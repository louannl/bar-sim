# simple dice function

import random


class DiceDecider:

    def __init__(self):
        self.dice_result = None

    # self explanatory! its a simple dice
    def dice_roll(self):
        self.dice_result = random.randint(1, 6)
        return self.dice_result

    # I got rid of 50/50 odds bc it was just this with more input options
    def is_even(self):
        self.dice_roll()
        return (self.dice_result % 2) == 0

    # this is for the pint element!
    def pint_increase_decider(self):
        self.dice_roll()
        if self.dice_result <= 2:
            return 1
        elif self.dice_result < 5:
            return 2
        else:
            return 3


