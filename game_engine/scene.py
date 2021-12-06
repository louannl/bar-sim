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


def scene_generator(scene_name: str, scene_data, game_state):
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
