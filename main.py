from dotenv import load_dotenv
from game_engine.character.character import Character
from game_engine.game import Game
from game_engine.scene.scene_manager import SceneManager
from save.end import End
from save.player import Player
from save.db_connection import DBConnection
from save.save import Save
from save.stats import Stats
from utils.utils import get_character, get_random_superhero, set_user_character
from utils.character_lists import player_options, superhero_list

'''
You only need to load dotenv once for the entire program in the main file,
it is not necessary to load it where os.getenv is used in each sub-module;
with exception to unit tests, which won't run main.py thus will need to load
env variables before running.
'''
load_dotenv()

db = DBConnection()
Game(
    Player(db, input("Please enter your name: ")),
    Character(get_character(set_user_character(player_options))),
    Character(get_character(get_random_superhero(superhero_list))),
    SceneManager(),
    Save(db),
    End(Stats(db))
).run()
