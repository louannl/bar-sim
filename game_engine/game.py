class Game:
    def __init__(self) -> None:
        self.main_character = 'Thomas The Tank Engine'
        self.superhero = 'Deadpool'
        self.prize = 'Stella Artois'
        self.pints = 0

    def update_main_character(self, character: str) -> None:
        self.main_character = character
