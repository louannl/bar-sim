import json
from os import error

from game_engine.game import Game
from game_engine.scene import scene_generator

with open("story/scenes.json") as jsonScenesFile:
    game_file = json.load(jsonScenesFile)
    game_scenes = game_file['scenes']
    jsonScenesFile.close()

game_state = Game()

scenario = 'introScene'
while scenario != 'end_scene':
    try:
        scenario = scene_generator(scenario, game_scenes, game_state)
    except error:
        # print(error)
        print('Sorry, something went wrong')
