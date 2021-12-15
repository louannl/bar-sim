import random

from utils.utils import set_user_character, get_character
from game_engine.character import Character


class Game:
    def __init__(self) -> None:
        '''
        These variables are used when preparing the scenes, so make sure the
        name of the variable matches the story scenes when necessary i.e.
        [main_character] [superhero] etc.
        '''
        self.superhero = Character(get_character(random.choice(list({60: "Bane", 69:"Batman", 97: "Black Canary", 309: "Harlequin", 322: "Hellboy", 522:"Poison Ivy", 374: "Juggernaut", 400: "Lady Deathstrike", 489: "Nick Fury"}))))
        self.prize = 'Stella Artois'
        self.pints = 0

    def update_main_character(self) -> None:
        self.main_character = Character(get_character(set_user_character())) #Will prompt user for inputs


# Example calls to get other superhero name and main_character name:
#accesses methods from Characters class
#
# example = Game()
#
# print(example.superhero.name)
#
# example.update_main_character()
# print(example.main_character.name)

