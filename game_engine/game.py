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

    def update_main_character(self, character: str) -> None:
        self.main_character = character

    def update_player_id(self, player_id: int) -> None:
        self.player_id = player_id
