### We have a json file with information about Pokemon that we want to collect into a dataframe. We will use the UniqueID as the pokemon name. Begin with the following code:

`import pandas as pd`

`import requests`

`req = requests.get('https://pastebin.com/raw/r1HwmQt0')`

`pokemon_dict = req.json()`

`pokemon_dict`

#### 1) Make a list containing every Pokemon name (UniqueID). Be careful of Pokemon "MOVE"s that are also in the top level. Your list should not include UniqueIDs that begin like this:"V0013\_MOVE". Only ones that are formatted like this: "V0013\_POKEMON". Your list length should be 151.


#### 2) Create two new lists. One should contain only the Pokemon name itself (e.g. 'BULBASAUR') with the 'V0001\_POKEMON\_' portion of the string removed. The other should have the Pokemon ID (e.g. 'V0001') stored as a string. All three lists should be the same length.

Note: There is one pokemon with two names separated by an underscore, don't worry about getting both parts of his name


#### 3) Create a dataframe with the ID (e.g. 'V0001') as the index and the pokemon name (e.g. 'Bulbasaur') as the first column.