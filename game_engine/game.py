import random

from game_engine.character import Character
from utils.utils import get_character


class Game:
    def __init__(self, main_character: str) -> None:
        '''
        These variables are used when preparing the scenes, so make sure the
        name of the variable matches the story scenes when necessary i.e.
        [main_character] [superhero] etc.
        '''
        main_character = main_character  # Character(get_character(set_user_character()))  #BUT THIS WILL ASK USER FOR INPUTS
        superhero = Character(get_character(str(random.randint(1, 731))))
        self.main_character = main_character.getName()
        self.superhero = superhero.getName()
        self.prize = 'Stella Artois'
        self.pints = 0

    def update_main_character(self, character: str) -> None:
        self.main_character = character
