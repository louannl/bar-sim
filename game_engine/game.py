from utils.utils import set_user_character, get_character
from game_engine.character import Character
from utils.utils import get_random_beer, random_insult


class Game:
    def __init__(self, main_character: Character, superhero: Character) -> None:
        """
        These variables are used when preparing the scenes, so make sure the
        name of the variable matches the story scenes when necessary i.e.
        [prize] [superhero] etc. (exception made for character classes!)
        """
        self.player_id = None
        self.main_character = main_character
        self.superhero = superhero
        self.pints = 9
        self.won = False
        self.prize = get_random_beer()
        self.insult = random_insult()

    def update_main_character(self, character: Character) -> None:
        self.main_character = character

    def update_superhero(self, superhero: Character) -> None:
        self.superhero = superhero

    def update_player_id(self, player_id: int) -> None:
        self.player_id = player_id

    def get_pints(self) -> int:
        return self.pints

    def get_player_id(self) -> int:
        return self.player_id

    def get_character_name(self) -> str:
        return self.main_character.getName()

    def get_win(self) -> bool:
        return self.won

    def victory(self) -> None:
        self.won = True

    def update_pints(self, amount):
        new_pints = self.pints + amount
        if new_pints <= 0:
            print('Oh no! No more pints are in your system!')
            self.pints = 0
            return 0
        self.pints = new_pints
        print('Current pints: ', self.pints)
        return self.pints
