import webbrowser

from utils.retry_decorator import retry_input
from game_engine.scene.scene import Scene
from game_engine.scene.dice import dice_scene
from game_engine.scene.too_sober import too_sober
from game_engine.scene.fight import fight_scene
from game_engine.scene.earthquake import earthquake_scene
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game_engine.game.game import Game


class SceneManager:
    @retry_input
    def get_choice(self, scene: Scene) -> int:
        print(scene.render_choices())
        return int(input('Pick: '))

    def handle_choice(self, scene: Scene) -> str:
        user_choice = self.get_choice(scene)
        if user_choice == 0:
            exit()

        print(scene.render_result(user_choice))
        return str(user_choice)

    def handle_next_scene(self, next_scene: str, game: 'Game') -> str:
        if next_scene == 'dice':
            return dice_scene(game)

        if next_scene == 'fightTime':
            return fight_scene(game)

        if next_scene == 'earthquake':
            return earthquake_scene(game)

        if next_scene == 'goHome':
            game.pint_counter.update_pints(-3)

        return next_scene

    def manage(self, scene: Scene, game: 'Game') -> str:
        if scene.return_name() == 'win':
            game.victory()

        if game.pint_counter.get_pints() <= 0:
            return too_sober()

        print(scene.render_intro({
            "main_character": game.main_character.getName(),
            "superhero": game.superhero.getName(),
            "pints": game.pint_counter.get_pints(),
            "prize": game.prize,
            "insult": game.insult
        }))

        if not scene.return_options():
            print('THE END')
            return 'end_scene'

        scene_choice = scene.options[self.handle_choice(scene)]
        if scene_choice['choice'] == 'Ask Rick':
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            return 'lose'

        return self.handle_next_scene(scene_choice['nextScene'], game)
