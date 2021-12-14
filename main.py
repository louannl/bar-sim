import json
from os import error
from beer_prize.beer_prize_animation import play_beer

from game_engine.game import Game
from game_engine.scene import Scene, scene_generator

with open("story/scenes.json") as jsonScenesFile:
    game_file = json.load(jsonScenesFile)
    game_scenes = game_file['scenes']
    jsonScenesFile.close()

game_state = Game()

scenario = 'introScene'
while scenario != 'end_scene':
    try:
        scenario = scene_generator(Scene(game_scenes[scenario]), game_state)
    except error:
        # print(error)
        print('Sorry, something went wrong')

play_beer()
