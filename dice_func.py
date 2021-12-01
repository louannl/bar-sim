# simple dice function

import random


class DiceDecider:

    def __init__(self):
        self.action = None
        self.dice_result = None
        self.count_of_tries = None

    # self explanatory! its a simple dice
    def dice_roll(self):
        self.dice_result = random.randint(1, 6)
        return self.dice_result

    # I got rid of 50/50 odds bc it was just this with more input options
    def is_even(self):
        self.dice_roll()
        return (self.dice_result % 2) == 0

    # this can be changed if we want to fix a number of retries, it also doesn't print every outcome
    def retry_action(self, func, max_retries):
        self.count_of_tries = 0
        while self.count_of_tries != max_retries:
            return func
        else:
            return False

    # this is for the pint element!
    def pint_increase_decider(self):
        if self.dice_roll() <= 2:
            return 1
        elif self.dice_roll() < 5:
            return 2
        else:
            return 3


