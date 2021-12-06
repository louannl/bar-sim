from game_engine.game import Game


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

    def render_choices(self):
        rendered_options = ''
        for option in self.options:
            rendered_options += f'{option}. {self.options[option]["choice"]}\n'
        return rendered_options

    def render_result(self, choice: int):
        return self.options[str(choice)]['action']


def get_options(scene):
    print(scene.render_choices())
    choice = int(input('Pick: '))
    return choice


def scene_generator(scene: Scene, game_state):
    scene_options = scene.return_options()
    print(scene.render_intro(game_state))

    if not scene_options:
        print('THE END')
        return 'end_scene'

    users_choice = get_options(scene)
    print(scene.render_result(users_choice))
    return scene.options[str(users_choice)]['nextScene']
