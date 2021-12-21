class Scene:
    def __init__(self, scene_name: str, scene: dict) -> None:
        self.scene_name = scene_name
        self.intro = scene['intro']
        self.options = scene['options']

    def return_name(self) -> dict:
        return self.scene_name

    def return_options(self) -> dict:
        return self.options

    def render_intro(self, game_vars: dict) -> str:
        transformed_intro = self.intro
        for key, value in game_vars.items():
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
