"""
Combine.py

This module contains the functions for combining elements.
"""

import json5 as json
from Modules.Library import HasCombination

def Combine(BACKEND, prompt, element_list, library):
    """
    Combine an element list.

    Args:
    BACKEND (dict): The backend dictionary.
    prompt (str): The system prompt pre formatted with the element list.
    element_list (list): The elements in list form.
    library (dict): The library dictionary.

    Returns:
    str: The combined element. or None if its impossible to combine the elements.
    dict: The updated library.
    """
    
    # Generate response from the backend
    response = BACKEND['Generate'](prompt)

    response = response.lstrip()
    response = response.rstrip()

    if response == None:
        return None, None
    
    if not response.endswith('}'):
        print(response[-1])
        response = response + '}'
    if response[0] != '"':
        response = '"' + response

    # Check if the response is valid JSON
    try:
        response_data = json.loads('{' + response + '}')
    except Exception as e:
        if None in response:
            return None, None
        
        print('Response from backend was not valid JSON, try again')
        print(f'Response:\n{response}')
        print(f'Exception: {e}')
        return None, None
    
    # Get the response element, emoji and description
    response_element = list(response_data.keys())[0]
    response_emoji = response_data[response_element]['Emoji']
    response_description = response_data[response_element]['Description']

    # If the reponse seems like valid JSON data but contains None, just return None
    if response_element == 'None':
        return None, None
    if response_emoji == 'None':
        return None, None
    if response_description == 'None':
        return None, None
    
    # If the response element has underscores in the name get rid of them
    if '_' in response_element:
        response_element = response_element.replace('_', '')
    
    # If the response element has spaces in the name get rid of them
    if ' ' in response_element:
        response_element = response_element.replace(' ', '')

    if response_element in library:
        response_origin = library[response_element]['Origin']
        
        if response_origin == 'Default':
            return response_element, library

        # If the origin list already has Element list or any combination of Element list
        if HasCombination(response_origin, element_list):
            # This element has already been created this way
            return response_element, library
        else:
            # This element has not been created this way
            response_origin.append(element_list)
            library[response_element]['Origin'] = response_origin

            return response_element, library
    
    library[response_element] = {
        'Emoji': response_emoji,
        'Description': response_description,
        'Origin': [element_list]
    }

    return response_element, library