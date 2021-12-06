class Scene():
    def __init__(self, scene: dict) -> None:
        self.intro = scene['intro']
        self.options = scene['options']

    def return_options(self) -> dict:
        return self.options

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


def scene_generator(scene: Scene, game_state):
    # TODO: This is really messy and has duplications that can be sorted out
    scene_options = scene.return_options()
    print(scene.render_intro(game_state.main_character,
          game_state.superhero, game_state.prize))

    if not scene_options:
        print('THE END')
        return 'end_scene'

    users_choice = get_options(scene)
    print(scene.render_result(users_choice))
    return scene.options[str(users_choice)]['nextScene']
