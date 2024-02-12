# LocalCraft

A simple remake of Neal Agarwal's InfiniteCraft using local LLMs to generate elements.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Python 3.x

### Installing

1. Clone the repository:
```
git clone https://github.com/yourusername/LocalCraft.git
```
2. If you want to use the langchain or openai backend, install the required packages using pip:
```
pip install -r langchain-requirements.txt
```
or
```
pip install -r openai-requirements.txt
```
3. Done!

## Usage

To start the game, run the following command:
```
python LocalCraft.py
```
There are 3 commands in the game:

* `!exit` - Exit the game
* `!WIPE` - Wipe the current generation
* `!autoplay` - Automatically generate new elements

Other then that the only inputs are the elements you want to combine

There are 3 backends for text generation available in `settings.json`.
The default backend is 'text-generation-webui'.

## Contributing

Contributions are greatly appreciated and are encouraged. If you have any ideas or suggestions, please open an issue or submit a pull request.

Note: The code base is probably messy and buggy at the current moment, so please be patient and feel free to contribute improvements.

## Authors

* Piper8x7b

# Is this overenginered?
Possibly. :'3