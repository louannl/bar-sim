# Game state

class Game:
    def __init__(self) -> None:
        self.main_character = ''
        self.pints = 0

    def increase_pints_randomly():
        # roll dice
        # 1-2: 1, 2-4: 2, 5-6: 3 pints
        pass


class Scene(Game):
    def __init__(self, intro: str, options: list) -> None:
        super().__init__()
        self.intro = intro
        self.options = options

    def render_options(self):
        for (index, option) in enumerate(self.options, start=1):
            print(f'{index}. {option}')


if __name__ == '__main__':
    game_state = Game()
    # Practice scene:
    name, barman = 'Zoe', 'Sunitha'
    intro = f'''It's a dark cold night outside the Coach and Horses Inn.
    You, {name}, walk into the bar...
    You approach the barman, {barman}. They growl at you:
    'What do ye want?'
    \n What do you do next?
    '''
    options = ['Ask for a cuppa tea, because you don\'t drink', 'Get a beer',
               'Throw an empty glass at the barman for not using proper grammar']

    intro_scene = Scene(intro, options)
    print(intro_scene.render_options())
    # starting_scene('Zoe', 'Sunitha')
