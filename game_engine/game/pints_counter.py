class PintCounter:
    def __init__(self) -> None:
        self.pints = 9

    def get_pints(self) -> int:
        return self.pints

    def update_pints(self, amount: int) -> int:
        new_pints = self.pints + amount
        if new_pints <= 0:
            print('Oh no! No more pints are in your system!')
            self.pints = 0
            return 0
        self.pints = new_pints
        print('Current pints: ', self.pints)
        return self.pints
