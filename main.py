from save.sendqueries import endgame
import json
from os import error

# I don't like comments, but I'm adding them for the sake of the team.
# TODO: Error handling i.e. try/except for user inputs etc.


class Game:
    def __init__(self, main_character: str, superhero: str) -> None:
        # TODO: Change this to auto-generate characters on initialization
        # Then we can remove inputting main_char/superhero
        self.main_character = main_character
        self.superhero = superhero
        self.prize = 'Stella Artois'
        self.pints = 0

    def increase_pints_randomly():
        # TODO: roll dice to increase pints
        # e.g. 1-2: 1, 2-4: 2, 5-6: 3 pints
        pass


class Scene():
    def __init__(self, intro: str, options='') -> None:
        self.intro = intro
        self.options = options

    def render_intro(self, main_character, superhero, prize):
        # Might be worth making this dynamic i.e. input game_state_characters (dict)
        # Then replace all those characters dynamically in any intro
        return self.intro.replace('[superhero]', superhero).replace(
            '[main_character]', main_character).replace('[prize]', prize)

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


def scene_generator(scene_name: str, scene_data):
    # TODO: This is really messy and has duplications that can be sorted out
    if 'options' not in scene_data[scene_name]:
        scene = Scene(
            scene_data[scene_name]['intro'],
            ''
        )
        print(scene.render_intro(game_state.main_character,
              game_state.superhero, game_state.prize))
        print('THE END')
        return 'end_scene'
    # Initialise scene with scene info
    scene = Scene(
        scene_data[scene_name]['intro'],
        scene_data[scene_name]['options']
    )
    # TODO: As mentioned above, we can look at making this dynamic
    print(scene.render_intro(game_state.main_character,
          game_state.superhero, game_state.prize))
    users_choice = get_options(scene)
    print(scene.render_result(users_choice))
    # TODO: Add functionality so if a choice has more than one nextScene (dependant)
    # on an event etc. this will run the event then return the success/failure scene
    return scene.options[str(users_choice)]['nextScene']


if __name__ == '__main__':
    # Read JSON file and return Game Scenes i.e. game_scenes
    with open("story/scenes.json") as jsonScenesFile:
        game_file = json.load(jsonScenesFile)
        game_scenes = game_file['scenes']
        jsonScenesFile.close()

    # # Let's run this to see if it works!
    game_state = Game('Thomas the Tank Engine', 'Deadpool')

    # # The starting scenario!
    scenario = 'introScene'

    while scenario != 'end_scene':
        try:
            scenario = scene_generator(scenario, game_scenes)
        except error:
            # print(error)
            print('Sorry, something went wrong')

    player_name = input('Please enter your name: ')
    character_name = 'antman'
    end_result = 'wine'
    endgame(player_name, character_name, end_result)