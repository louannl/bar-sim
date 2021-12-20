from game_engine.game import Game
from utils.dice_decider import DiceDecider
import time


def dice_scene(game_state: Game) -> str:
    time.sleep(1)
    print('You chuck the dice high, it falls...')
    time.sleep(5)
    dice_decider = DiceDecider()
    roll_amount = dice_decider.dice_roll()
    print(f'You rolled a {roll_amount}')
    if roll_amount > 3:
        time.sleep(1)
        print('Success!')
        time.sleep(3)
        game_state.update_pints(2)
        return 'win'
    time.sleep(1)
    print('oh no... how unlucky...')
    game_state.update_pints(-2)
    time.sleep(3)
    return 'lose'
