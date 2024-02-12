"""
AutoPlay.py

This module contains the functions for auto playing.
"""

import json5 as json
import random
from Modules.Library import GetAllTestedCombinations

# Load settings
settings = json.load(open('settings.json'))

def Lerp(start, end, t):
    """
    Simple lerp function.

    Args:
    start (float): The start value.
    end (float): The end value.
    t (float): The t value.

    Returns:
    float: The lerped value.
    """
    return start + (end - start) * t

def GenerateWeightsForElements(library):
    """
    Generate weights for elements.

    Args:
    library (dict): The library dictionary.

    Returns:
    list: The weights list.
    """
    # Im just not going to comment on this function, it's a mess
    len_library = len(library)

    weights = [0] * len_library

    favor_n = settings['Auto-Play']['Perfer-New-Elements-FavorN-Ratio']
    favor_weight_start = settings['Auto-Play']['Perfer-New-Elements-Weight-Old']
    favor_weight_end = settings['Auto-Play']['Perfer-New-Elements-Weight-New']
    preference_weight = settings['Auto-Play']['Prefer-New-Elements-Weight-Curve']

    if favor_n >= len_library:
        favor_n = favor_n - 1
    elif favor_n <= 0:
        favor_n = 1
    ramp_up_n = len_library - favor_n

    delta = (favor_weight_end - favor_weight_start) / (ramp_up_n ** preference_weight)
    for i in range(ramp_up_n):
        weights[i] = favor_weight_start + delta * (i ** preference_weight)
    for i in range(ramp_up_n, len(library)):
        weights[i] = favor_weight_end

    # The first four elements are default and should have the max weight
    weights[0] = favor_weight_end
    weights[1] = favor_weight_end
    weights[2] = favor_weight_end
    weights[3] = favor_weight_end

    return weights

def GetRandomElementsWeighted(library, weights):
    """
    Get a set of two random elements based on the weights

    Args:
    library (dict): The library dictionary.
    weights (list): The weights list.

    Returns:
    str: The element.
    """
    # Itterate until a valid pair is found
    # TODO: This can probably be sped up
    element1, element2 = random.choices(list(library.keys()), weights=weights, k=2)
    while element1 == element2:
        element1, element2 = random.choices(list(library.keys()), weights=weights, k=2)
    while (element1, element2) in GetAllTestedCombinations() or (element2, element1) in GetAllTestedCombinations() or element1 == element2:
        element1, element2 = random.choices(list(library.keys()), weights=weights, k=2)
    return element1, element2

def GetRandomElements(library):
    """
    Get a set of two random elements

    Args:
    library (dict): The library dictionary.

    Returns:
    str: The element.
    """
    # Itterate until a valid pair is found
    # TODO: This can probably be sped up
    while True:
        element1, element2 = random.sample(list(library.keys()), 2)
        if (element1, element2) not in GetAllTestedCombinations() or (element2, element1) not in GetAllTestedCombinations():
            return element1, element2

def AutoPlay(library):
    """
    Auto play function

    Args:
    library (dict): The library dictionary.

    Returns:
    str: The elements.
    """
    # Get a set of two random elements and return them
    if settings['Auto-Play']['Prefer-New-Elements']:
        weights = GenerateWeightsForElements(library)
        element1, element2 = GetRandomElementsWeighted(library, weights)
    else:
        element1, element2 = GetRandomElements(library)
    return element1, element2
