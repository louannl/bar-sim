from random import randint
from game_engine.character import Character
from game_engine.game import Game
from utils.decorators import retry_input
from utils.dice_decider import DiceDecider
import webbrowser
import time

from utils.fight import FightClub


class Scene:
    def __init__(self, scene: dict) -> None:
        self.intro = scene['intro']
        self.options = scene['options']

    def return_options(self) -> dict:
        return self.options

    def render_intro(self, game_state: Game) -> str:
        game_state_variables = vars(game_state).items()
        transformed_intro = self.intro
        for key, value in game_state_variables:
            if isinstance(value, Character):
                value = value.getName()
            transformed_intro = transformed_intro.replace(
                f'[{key}]', str(value))
        return transformed_intro

    def render_choices(self) -> str:
        rendered_options = ''
        for option in self.options:
            rendered_options += f'{option}. {self.options[option]["choice"]}\n'
        rendered_options += '0. Quit Game\n'
        return rendered_options

    def render_result(self, choice: int) -> str:
        return self.options[str(choice)]['action']


def get_choice(scene: Scene) -> int:
    print(scene.render_choices())
    return int(input('Pick: '))


@retry_input
def scene_generator(scene: Scene, game_state: Game) -> str:
    if game_state.pints <= 0:
        return too_sober()

    scene_options = scene.return_options()
    print(scene.render_intro(game_state))

    if not scene_options:
        print('THE END')
        return 'end_scene'

    user_choice = get_choice(scene)

    if user_choice == 0:
        exit()

    print(scene.render_result(user_choice))

    scene_choice = scene.options[str(user_choice)]
    if scene_choice['choice'] == 'Ask Rick':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        return 'lose'

    next_scene = scene_choice['nextScene']

    if next_scene == 'dice':
        return dice_scene(game_state)

    if next_scene == 'fightTime':
        return fight_scene(game_state)

    if next_scene == 'goHome':
        game_state.update_pints(-3)

    if next_scene == 'win':
        game_state.victory()

    if next_scene == 'earthquake':
        return earthquake_scene()

    return next_scene


def earthquake_scene(game_state: Game) -> None:
    time.sleep(3)
    print("The murky flagstones cleave and fracture as you abandon all thoughts of pints or bars and simply play hopscotch at the end of days.\nThe earth itself seems to breaking into a grin, presenting a gaping crevasse that prepares for your descent, but before you slip into it, someone grabs your legs and hauls you back, under a table.\nIt's the other barkeep.  You hope that your deep appreciation can be read from your eyes.\nBefore you can speak, an aftershock thrusts you together, while rubble and debris engulf the table above.  You're sealed in.\n So. This is how it ends.\nYou cling to each other.")
    time.sleep(3)
    choice = randint(1, 2)
    if choice == 1:
        print('You attempt to push the rubble to break free')
        return strength_scene_test(game_state)
    print('There\'s only one way to survive the rubble... Roll-a-dice..')
    return dice_scene(game_state)


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


def strength_scene_test(game_state: Game) -> str:
    print('You push with all your might!')
    time.sleep(5)
    char_str = game_state.main_character.strength
    print(f'Your chosen character\'s strength is: {char_str}')
    if int(char_str) > 30:
        print('You push it way, and save yourself and the barman! \nAs you struggle for the door, the barman grabs a pint for you...')
        time.sleep(3)
        game_state.update_pints(2)
        time.sleep(1)
        return 'win'
    time.sleep(5)
    print('You\'re not strong enough, you\'re pushed back by the force...Oh no...')
    game_state.update_pints(-2)
    time.sleep(3)
    return 'lose'


def fight_scene(game_state: Game) -> str:
    fight_club = FightClub(game_state.superhero, game_state.main_character)
    fight_result = fight_club.activate_rounds_get_outcome()
    if fight_result:
        game_state.update_pints(2)
        return 'win'
    game_state.update_pints(-2)
    return 'fightTime'


def too_sober() -> str:
    print('You failed to get enough pints and became too *sober*\nYou are now Tee-Total...')
    print('THE END')
    return 'end_scene'
