import json
from os import error

from game_engine.game import Game
from game_engine.scene import Scene, scene_generator
from utils.return_player_id import create_or_return_player_id


with open("story/scenes.json") as jsonScenesFile:
    game_file = json.load(jsonScenesFile)
    game_scenes = game_file['scenes']
    jsonScenesFile.close()

game_state = Game()

player_name = input("Please enter your name: ")
create_or_return_player_id(player_name, game_state)

scenario = 'introScene'
while scenario != 'end_scene':
    try:
        scenario = scene_generator(Scene(game_scenes[scenario]), game_state)
    except error:
        # print(error)
        print('Sorry, something went wrong')

