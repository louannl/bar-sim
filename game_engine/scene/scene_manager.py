import webbrowser
from game_engine.game import Game
from utils.retry_decorator import retry_input
from game_engine.scene.scene import Scene
from game_engine.scene.dice import dice_scene
from game_engine.scene.too_sober import too_sober
from game_engine.scene.fight import fight_scene
from game_engine.scene.earthquake import earthquake_scene


def get_choice(scene: Scene) -> int:
    print(scene.render_choices())
    return int(input('Pick: '))


@retry_input
def scene_manager(scene: Scene, game_state: Game) -> str:
    if game_state.pints <= 0:
        return too_sober()

    scene_options = scene.return_options()
    print(scene.render_intro(game_state))

    if not scene_options:
        print('THE END')
        return 'end_scene'

    user_choice = get_choice(scene)

    if user_choice == 0:
        exit()

    print(scene.render_result(user_choice))

    scene_choice = scene.options[str(user_choice)]
    if scene_choice['choice'] == 'Ask Rick':
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        return 'lose'

    next_scene = scene_choice['nextScene']

    if next_scene == 'dice':
        return dice_scene(game_state)

    if next_scene == 'fightTime':
        return fight_scene(game_state)

    if next_scene == 'goHome':
        game_state.update_pints(-3)

    if next_scene == 'earthquake':
        return earthquake_scene(game_state)

    if next_scene == 'win':
        game_state.victory()

    return next_scene
