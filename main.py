import json
from beer_prize.beer_prize_animation import play_beer
from game_engine.game import Game
from game_engine.scene import Scene, scene_generator
from game_engine.character import Character
from save.save_game import GetGameHistory
from save.query import Query
from utils.save_helpers import (
    create_or_return_player_id,
    return_play_and_win_count,
    save_game
)
from utils.utils import get_character, get_random_superhero, set_user_character
from utils.character_lists import player_options, superhero_list

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
        scenario = scene_generator(Scene(game_scenes[scenario]), game_state)
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
