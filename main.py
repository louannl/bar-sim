import json
from os import error

from game_engine.game import Game
from game_engine.scene import Scene, scene_generator
from save.player import CheckPlayer, CreatePlayer
from save.query import Query


with open("story/scenes.json") as jsonScenesFile:
    game_file = json.load(jsonScenesFile)
    game_scenes = game_file['scenes']
    jsonScenesFile.close()

game_state = Game()
# Getting player name
player_name = input("Please enter your name: ")
# Checking if player already exists
player = CheckPlayer(Query())
player_exists = player.check_player(player_name)
# getting player id
if not player_exists:
    print(player_exists, "if not")
    new_player = CreatePlayer(Query())
    new_player.create_player(player_name)
    player_exists = player.check_player(player_name)

game_state.update_player_id(player_exists[0][0])
print(game_state.player_id)


scenario = 'introScene'
while scenario != 'end_scene':
    try:
        scenario = scene_generator(Scene(game_scenes[scenario]), game_state)
    except error:
        # print(error)
        print('Sorry, something went wrong')

# TODO: Uncomment this
# end_result = game_state.prize
# endgame(player_name, character_name, end_result)
