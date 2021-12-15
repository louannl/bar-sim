class Game:
    def __init__(self) -> None:
        '''
        These variables are used when preparing the scenes, so make sure the
        name of the variable matches the story scenes when necessary i.e.
        [main_character] [superhero] etc.
        '''
        self.player_id = None
        self.main_character = 'Thomas The Tank Engine'
        self.superhero = 'Deadpool'
        self.prize = 'Stella Artois'
        self.pints = 0
        self.won = False

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
