import json

# I don't like comments, but I'm adding them for the sake of the team.
# TODO: Error handling i.e. try/except for user inputs etc.


class Game:
    def __init__(self, main_character: str, barman: str) -> None:
        # TODO: We can change this to auto generate on start?
        self.main_character = main_character
        self.barman = barman
        self.pints = 0

    def increase_pints_randomly():
        # TODO: roll dice to increase pints
        # e.g. 1-2: 1, 2-4: 2, 5-6: 3 pints
        pass


class Scene():
    def __init__(self, intro: str, options) -> None:
        self.intro = intro
        self.options = options

    def render_intro(self, main_character, barman):
        return self.intro.replace('{{BARMAN}}', barman).replace(
            '{{MAIN_CHARACTER}}', main_character)

    def render_choices(self):
        rendered_options = ''
        for option in self.options:
            rendered_options += f'{option}. {self.options[option]["choice"]}\n'
        return rendered_options

    def render_result(self, choice: int):
        return self.options[str(choice)]['action']


def scene_generator(scene_name: str, scene_data):
    # Initialise scene with scene info
    scene = Scene(
        scene_data[scene_name]['intro'],
        scene_data[scene_name]['options']
    )
    # Render intro of the scene (need to make dynamic!!!)
    print(scene.render_intro(game_state.main_character, game_state.barman))
    print(scene.render_choices())
    choice = int(input('Pick: '))
    print(scene.render_result(choice))

# TODO: Create a loop that uses the scene then moves on to the next scene
# TODO: Add functionality to have succesful and failures in the scenes (see JSON)


if __name__ == '__main__':
    # Checking it works!!!
    game_state = Game('Thomas the Tank Engine', 'Terry the barman')

    # Read JSON file and return Game Scenes i.e. game_scenes
    with open("scenes.json") as jsonScenesFile:
        game_file = json.load(jsonScenesFile)
        game_scenes = game_file['scenes']
        jsonScenesFile.close()

    # Start with introScene
    scene_generator('introScene', game_scenes)
    # Checking whether barScene replaces 'barman' with game state barman
    scene_generator('barScene', game_scenes)
