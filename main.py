import json
import random
from os import error

from hero_class import Superhero
from utils.utils import get_character
from utils.dice_decider import DiceDecider


# I don't like comments, but I'm adding them for the sake of the team.
# TODO: Error handling i.e. try/except for user inputs etc.


class Game:
    def __init__(self, main_character: str) -> None:
        main_character = main_character  # Superhero(get_character(set_user_character()))  #BUT THIS WILL ASK USER FOR INPUTS
        superhero = Superhero(get_character(str(random.randint(1, 731))))
        self.main_character = main_character.getName()
        self.superhero = superhero.getName()
        self.prize = 'Stella Artois'
        self.pints = 0

    def increase_pints_randomly():
        roll_of_dice = DiceDecider()
        num = roll_of_dice.dice_roll()
        roll_of_dice.decide_increase_amount(num)


class Scene():
    def __init__(self, intro: str, options = '') -> None:
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
