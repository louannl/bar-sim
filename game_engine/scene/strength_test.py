
from game_engine.game import Game
import time


def strength_scene_test(game_state: Game) -> str:
    print('You push with all your might!')
    time.sleep(5)
    char_str = game_state.main_character.strength
    print(f'Your chosen character\'s strength is: {char_str}')
    if int(char_str) > 30:
        print(
            'You push it way, and save yourself and the barman! \nAs you '
            'struggle for the door, the barman grabs a pint for you...'
        )
        time.sleep(3)
        game_state.update_pints(2)
        time.sleep(1)
        return 'win'
    time.sleep(5)
    print(
        'You\'re not strong enough, you\'re pushed back by the force...Oh '
        'no...'
    )
    game_state.update_pints(-2)
    time.sleep(3)
    return 'lose'
