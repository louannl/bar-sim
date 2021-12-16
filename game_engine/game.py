from utils.utils import get_random_beer, random_insult


class Game:
    def __init__(self) -> None:
        """
        These variables are used when preparing the scenes, so make sure the
        name of the variable matches the story scenes when necessary i.e.
        [main_character] [superhero] etc.
        """
        self.player_id = None
        self.main_character = 'Thomas The Tank Engine'
        self.superhero = 'Deadpool'
        self.pints = 9
        self.won = False
        self.prize = get_random_beer()
        self.insult = random_insult()

    def update_main_character(self, character: str) -> None:
        self.main_character = character

    def update_player_id(self, player_id: int) -> None:
        self.player_id = player_id

    def get_pints(self) -> int:
        return self.pints

    def get_player_id(self) -> int:
        return self.player_id

    def get_character(self) -> str:
        return self.main_character

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
