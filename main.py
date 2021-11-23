import json

# Game state


class Game:
    def __init__(self, main_character: str) -> None:
        self.main_character = main_character
        self.pints = 0

    def increase_pints_randomly():
        # TODO: roll dice
        # 1-2: 1, 2-4: 2, 5-6: 3 pints
        pass


class Scene(Game):
    def __init__(self, main_character: str, intro: str, options) -> None:
        super().__init__(main_character)
        self.intro = intro
        self.options = options

    def render_choices(self):
        rendered_options = ''
        for option in self.options:
            rendered_options += f'{option}. {self.options[option]["choice"]}\n'
        return rendered_options


if __name__ == '__main__':
    game_state = Game('Thomas the Tank Engine')
    # testing scene:

    # get json data from scenes.json
    with open("scenes.json") as jsonScenesFile:
        game_file = json.load(jsonScenesFile)
        game_scenes = game_file['scenes']
        jsonScenesFile.close()

    # get introscene info from scenes.json
    introScene = game_scenes['introScene']

    # Create a scene using introscene info
    intro_scene = Scene(
        'Thomas the Tank Engine',
        introScene['intro'],
        introScene['options']
    )
    # Render intro of the scene (need to make dynamic!!!)
    print(intro_scene.intro)
    # Render options
    print(intro_scene.render_choices())
