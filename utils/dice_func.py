import random


class DiceDecider:

    def __init__(self):
        self.dice_result = None

    def dice_roll(self):
        dice_result = random.randint(1, 6)
        return dice_result

    def is_even(self, num):  # odd_or_even
        return (num % 2) == 0

    def pint_increase_decider(self, num):
        if num <= 2:
            return 1
        elif num < 5:
            return 2
        else:
            return 3  # exit()

    def pint_increase(self):
        return self.pint_increase_decider(self.dice_roll())

    # CHECKING WITH ZOE IF READY TO MERGE WITH REFACTORED DICEDECIDER CLASS AND TEST?
    # def try_action(action):
    #     if odd_or_even(dice_roll()):
    #         print("Success! You have managed to {}".format(action))
    #     else:
    #         try_new_thing = input("Oh no! You failed to {}, would you like to try something else? y/n ".format(action))
    #         if try_new_thing == 'y':
    #             action = input("What would you like to try instead? ")
    #             try_action(action)
