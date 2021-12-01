from End_Of_Game import EndOfGame, Query
import json
from os import error

def main():
# I don't like comments, but I'm adding them for the sake of the team.
# TODO: Error handling i.e. try/except for user inputs etc.


class Game:
    def __init__(self, main_character: str, barman: str) -> None:
        # TODO: Change this to auto-generate characters on initialization
        # Then we can remove inputting main_char/barman
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
        # Might be worth making this dynamic i.e. input game_state_characters (dict)
        # Then replace all those characters dynamically in any intro
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
    # TODO: As mentioned above, we can look at making this dynamic
    print(scene.render_intro(game_state.main_character, game_state.barman))
    print(scene.render_choices())
    choice = int(input('Pick: '))
    print(scene.render_result(choice))
    # TODO: Add functionality so if a choice has more than one nextScene (dependant)
    # on an event etc. this will run the event then return the success/failure scene
    return scene.options[str(choice)]['nextScene']


if __name__ == '__main__':
    # Read JSON file and return Game Scenes i.e. game_scenes
    with open("story/scenes.json") as jsonScenesFile:
        game_file = json.load(jsonScenesFile)
        game_scenes = game_file['scenes']
        jsonScenesFile.close()

    # Let's run this to see if it works!
    game_state = Game('Thomas the Tank Engine', 'Terry the barman')

    # The starting scenario!
    scenario = 'introScene'
    # We don't have endScene or error handling, so I've limited this to avoid
    # an infinite loop!
    count = 0
    while scenario != 'endScene':
        try:
            if count > 5:
                # To avoid an infinite loop
                break
            scenario = scene_generator(scenario, game_scenes)
            count += 1
        except error:
            print(error)

    # TODO: Run the endscene sequence!
    finish = EndOfGame()
    game_time_string = finish.save()
    database_queries = Query()
    database_queries.send_all_queries(player_name, game_character, game_time_string, end_result)
    ### need to define player_name, game_character, end_result ###



