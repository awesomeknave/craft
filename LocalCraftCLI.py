"""
LocalCraftCLI.py

LocalCraft is a simple remake of Neal Agarwal's InfiniteCraft using local LLMs to generate elements.
This file is the CLI frontend of LocalCraft.
"""

from Modules.Backend import BACKEND as BACKEND
import Modules.Prompt as Prompt
import Modules.Combine as Combine
import Modules.AutoPlay as AutoPlay
import Modules.Library as Library

import json5 as json

def RunGame():
    running = True
    autoplay = False

    while running:
        # Display the library
        Library.DisplayLibrary()
        print('Total possible new two element combinations: ' + str(Library.GetTotalPossibleUntestedCombinations()))

        if autoplay:
            element1, element2 = AutoPlay.AutoPlay(Library.GetLibrary())
            element_list = [f'{element1}, {element2}']

            print('Input: ' + json.dumps(element_list))
            
            prompt = Prompt.FillInSystemPrompt(element_list, Library.GetLibrary())
            response, library = Combine.Combine(BACKEND, prompt, element_list, Library.GetLibrary())
            print('Output: ' + response)

            # Save the library
            Library.SaveLibrary(library)
            continue

        # Get input
        element_list = input('Input: ')

        if element_list.startswith('!'):
            if element_list == '!exit':
                running = False
                break
            elif element_list == '!WIPE':
                print('Are you sure you want to WIPE the library? (This will delete all progress and can not be undone) (y/n)')
                if input().lower() == 'y':
                    # Replace Library.json with a new copy of Library-Default.json
                    Library.WipeLibrary()
                    print('Library wiped!')
                    continue
                else:
                    print('Aborting WIPE')
                    continue
            elif element_list == '!autoplay':
                print('Are you sure you want to enable AutoPlay? (This will cease all inputs until the game is restarted) (y/n)')
                if input().lower() == 'y':
                    autoplay = True
                    print('AutoPlay enabled!')
                    continue
                else:
                    print('Aborting AutoPlay')
                    continue
        
        elements = element_list.split(', ')

        element_list_josn = '['
        for element in elements:
            element_list_josn += '"' + element + '", '
        
        element_list = json.loads(element_list_josn[:-2] + ']')

        prompt = Prompt.FillInSystemPrompt(element_list, Library.GetLibrary())
        response, library = Combine.Combine(BACKEND, prompt, element_list, Library.GetLibrary())
        print('Output: ' + str(response))

        # Save the library
        if library is not None:
            Library.SaveLibrary(library)
        

if __name__ == '__main__':
    RunGame()