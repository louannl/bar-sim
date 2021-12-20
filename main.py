import json
from dotenv import load_dotenv
from beer_prize.beer_prize_animation import play_beer
from game_engine.character.character import Character
from game_engine.game import Game
from game_engine.scene.scene import Scene
from game_engine.scene.scene_manager import scene_manager
from save.save_game import GetGameHistory
from save.query import Query
from utils.save_helpers import (
    create_or_return_player_id,
    return_play_and_win_count,
    save_game
)
from utils.utils import get_character, get_random_superhero, set_user_character
from utils.character_lists import player_options, superhero_list

'''
You only need to load dotenv once for the entire program in the main file,
it is not necessary to load it where os.getenv is used in each sub-module;
with exception to unit tests, which won't run main.py thus will need to load
env variables before running.
'''

load_dotenv()

with open("story/scenes.json") as jsonScenesFile:
    game_file = json.load(jsonScenesFile)
    game_scenes = game_file['scenes']
    jsonScenesFile.close()

player_name = input("Please enter your name: ")

player_character_id = set_user_character(player_options)

game_state = Game(
    Character(get_character(player_character_id)),
    Character(get_character(get_random_superhero(superhero_list)))
)

create_or_return_player_id(player_name, game_state)

scenario = 'introScene'
while scenario != 'end_scene':
    try:
        scenario = scene_manager(Scene(game_scenes[scenario]), game_state)
    except Exception as e:
        print('Sorry, something went wrong')
        print('Error: ', e)

save_game(game_state)
wins, plays = return_play_and_win_count(game_state)
print(
    f'You have played {plays} time{"s" if plays > 1 else ""}, and won {wins} '
    f'time{"s" if wins > 1 else ""}'
)
print(GetGameHistory(Query()).display_leaderboard())

play_beer()
