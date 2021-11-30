# simple dice function

import random


def dice_roll():
    dice_result = random.randint(1, 6)
    return dice_result


def odd_or_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False


def try_action(action):
    if odd_or_even(dice_roll()):
        print("Success! You have managed to {}".format(action))
    else:
        try_new_thing = input("Oh no! You failed to {}, would you like to try something else? y/n ".format(action))
        if try_new_thing == 'y':
            action = input("What would you like to try instead? ")
            try_action(action)
        else:
            exit()


