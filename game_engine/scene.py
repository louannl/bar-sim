from game_engine.character import Character
from game_engine.game import Game
from utils.dice_decider import DiceDecider


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

    next_scene = scene.options[str(user_choice)]['nextScene']

    if next_scene == 'dice':
        return dice_scene()

    if next_scene == 'goHome':
        game_state.update_pints(-3)

    if next_scene == 'win':
        game_state.victory()

    return next_scene


def dice_scene() -> str:
    print('You chuck the dice high, it falls...')
    dice_decider = DiceDecider()
    roll_amount = dice_decider.dice_roll()
    print(f'You rolled a {roll_amount}')
    if roll_amount > 3:
        print('Success!')
        return 'win'
    print('oh no... how unlucky...')
    return 'lose'


def too_sober() -> str:
    print('You failed to get enough pints and became too *sober*\nYou are now Tee-Total...')
    print('THE END')
    return 'end_scene'
