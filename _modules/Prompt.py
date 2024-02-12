"""
Prompt.py

This module loads the system prompt and contains functions for engineering prompts.
"""

import json5 as json

# Load settings
settings = json.load(open('settings.json'))

# Load and refactor the system prompt
with open(settings['System-Prompt'], 'r') as f:
    system_prompt = '\n'.join(line.strip() for line in f if not line.startswith('//'))

def FillInSystemPrompt(input_elements_str, library):
    """
    Fill in the system prompt with the required variables.
    
    Args:
    input_str (str): The input string to be filled in the system prompt.
    library (dict): The library to be used in the prompt
    
    Returns:
    str: The filled-in system prompt.
    """
    # Replace the input variable
    new_prompt = system_prompt
    new_prompt = new_prompt.replace('<input>', json.dumps(input_elements_str))

    # Replace the library variable if applicable
    if '<library>' in system_prompt:
        new_prompt = new_prompt.replace('<library>', json.dumps(library))

    # Replace the library condenced variable if applicable
    if '<library-condenced>' in system_prompt:
        # Create a minified version of the library with just the element names and emojis
        library_condenced = {}
        for key, value in library.items():
            library_condenced[key] = value['Emoji']
        
        new_prompt = new_prompt.replace('<library-condenced>', json.dumps(library_condenced))

    # Replace the library elements variable if applicable
    if '<library-elements>' in system_prompt:
        # Create a minified version of the library with just the element names
        library_elements = []
        for key in library_condenced:
            library_elements.append(key)
        
        new_prompt = new_prompt.replace('<library-elements>', json.dumps(library_elements))

    # Return the filled in prompt
    return new_prompt