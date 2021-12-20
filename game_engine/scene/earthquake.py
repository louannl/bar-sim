import time
from random import randint
from game_engine.game import Game
from game_engine.scene.dice import dice_scene
from game_engine.scene.strength_test import strength_scene_test


def earthquake_scene(game_state: Game) -> None:
    time.sleep(3)
    print(
        "The murky flagstones cleave and fracture as you abandon all thoughts"
        " of pints or bars and simply play hopscotch at the end of days."
    )
    time.sleep(1)
    print("The earth itself seems to breaking into a grin, presenting a gaping"
          " crevasse that prepares for your descent,\n "
          "...but before you slip into it,"
          " someone grabs your legs and hauls you back, under a table."
          )
    time.sleep(1)
    print(
        "It's the other barkeep.  You hope that your deep appreciation can be"
        " read from your eyes...\n"
    )
    time.sleep(1)
    print(
        "Before you can speak, an aftershock thrusts you together, "
        " while rubble and debris engulf the table above.  You're sealed in.\n"
        " So. This is how it ends.\nYou cling to each other."
    )
    choice = randint(1, 2)
    if choice == 1:
        print('You attempt to push the rubble to break free')
        return strength_scene_test(game_state)
    print('There\'s only one way to survive the rubble... Roll-a-dice..')
    return dice_scene(game_state)
