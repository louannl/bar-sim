import json
from os import error
from beer_prize.beer_prize_animation import play_beer

from game_engine.game import Game
from game_engine.scene import Scene, scene_generator
from utils.save_helpers import create_or_return_player_id, return_play_and_win_count, save_game


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

save_game(game_state)
wins, plays = return_play_and_win_count(game_state)
print(f'You have players {plays} amount of times, and won {wins} time/s')
play_beer()
