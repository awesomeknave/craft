"""
Library.py

This module loads the library and contains functions for manipulating the library.
"""

import json5 as json

# Load the library
with open('Library.json', 'r') as f:
    library = json.load(f)

def HasCombination(arr, ElementList):
    """
    Check the orgins of an element list to see if it has a combination
    """

    # TODO: This can be sped up by only checking the origin list
    for inner_arr in arr:
        if set(inner_arr).issubset(set(ElementList)):
            return True
    return False

def GetAllTestedCombinations():
    """
    Get all the combinations that have already been tested
    """
    combinations = set()
    for element in library.values():
        if 'Origin' in element and element['Origin'] != 'Default':
            for origin in element['Origin']:
                combinations.add(tuple(sorted(origin)))
    return combinations

def GetTotalPossibleUntestedCombinations():
    """
    Get the total number of two element combinations that can be tested
    """
    num_elements = len(library)
    total_combinations = num_elements * (num_elements - 1) // 2
    previously_combined_pairs = len(GetAllTestedCombinations())
    return total_combinations - previously_combined_pairs

def DisplayLibrary():
    """
    Display the library
    """

    print('### Library')
    for key, value in library.items():
        print(f'{key}, emoji: {value["Emoji"]}, description: {value["Description"]}')

def WipeLibrary():
    """
    Wipe the library
    """

    with open('Library.json', 'w') as f:
        json.dump(json.load(open('LibraryDefault.json')), f, indent=4)

def SaveLibrary(new_library):
    """
    Save the library
    """

    library = new_library

    with open('Library.json', 'w') as f:
        json.dump(library, f, indent=4, trailing_commas=False, quote_keys=True)

def GetLibrary():
    """
    Get the library
    """

    return library