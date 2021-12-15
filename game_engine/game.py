from utils.utils import random_insult


class Game:
    def __init__(self) -> None:
        '''
        These variables are used when preparing the scenes, so make sure the
        name of the variable matches the story scenes when necessary i.e.
        [main_character] [superhero] etc.
        '''
        self.main_character = 'Thomas The Tank Engine'
        self.superhero = 'Deadpool'
        self.prize = 'Stella Artois'
        self.pints = 0
        self.insult = random_insult()

    def update_main_character(self, character: str) -> None:
        self.main_character = character
