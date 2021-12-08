import random


class DiceDecider:

    def __init__(self):
        self.dice_result = None

    def dice_roll(self):
        dice_result = random.randint(1, 6)
        return dice_result

    def is_even(self, num):
        return (num % 2) == 0

    def pint_increase_decider(self, num):
        if num <= 2:
            return 1
        elif num < 5:
            return 2
        else:
            return 3

    def pint_increase(self):
        return self.pint_increase_decider(self.dice_roll())
