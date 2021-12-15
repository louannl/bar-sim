from game_engine.game import Game
from utils.dice_decider import DiceDecider
from utils.utils import random_insult


class Scene():
    def __init__(self, scene: dict) -> None:
        self.intro = scene['intro']
        self.options = scene['options']

    def return_options(self) -> dict:
        return self.options

    def render_intro(self, game_state: Game) -> str:
        game_state_variables = vars(game_state).items()
        transformed_intro = self.intro
        for key, value in game_state_variables:
            transformed_intro = transformed_intro.replace(
                f'[{key}]', str(value))
        return transformed_intro

    def render_choices(self) -> str:
        rendered_options = ''
        for option in self.options:
            rendered_options += f'{option}. {self.options[option]["choice"]}\n'
        return rendered_options

    def render_result(self, choice: int) -> str:
        return self.options[str(choice)]['action']


def get_choice(scene: Scene) -> int:
    print(scene.render_choices())
    return int(input('Pick: '))


def scene_generator(scene: Scene, game_state: Game) -> str:
    scene_options = scene.return_options()
    print(scene.render_intro(game_state))

    if type(scene_options) == list:
        print(scene_options)

    if not scene_options:
        print('THE END')
        return 'end_scene'

    users_choice = get_choice(scene)
    print(scene.render_result(users_choice))

    next_scene = scene.options[str(users_choice)]['nextScene']

    if next_scene == 'dice':
        return dice_scene()

    return next_scene


def dice_scene():
    print('You chuck the dice high, it falls...')
    dice_decider = DiceDecider()
    roll_amount = dice_decider.dice_roll()
    print(f'You rolled a {roll_amount}')
    if roll_amount > 3:
        print('Success!')
        return 'win'
    print('oh no... how unlucky...')
    return 'lose'
