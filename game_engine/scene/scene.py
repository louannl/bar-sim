from game_engine.character import Character
from game_engine.game import Game


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
