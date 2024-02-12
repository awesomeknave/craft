"""
LocalCraft.py

LocalCraft is a simple remake of Neal Agarwal's InfiniteCraft using local LLMs to generate elements.
This file is the main file of LocalCraft. This script simply runs the selected frontend.
"""

import json5 as json

# Load settings
settings = json.load(open('settings.json'))
frontend = settings['User-Interface']

# Run the selected frontend

if frontend == 'CLI':
    import LocalCraftCLI
    LocalCraftCLI.RunGame()
else:
    raise ValueError('Unknown frontend: ' + frontend)