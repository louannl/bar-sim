from game_engine.character.character import Character
from game_engine.scene.scene import Scene
from game_engine.scene.scene_manager import SceneManager
from save.end import End
from save.player import Player
from save.save import Save
from story.import_json import import_json
from utils.utils import get_random_beer, random_insult


class Game:
    def __init__(
        self,
        player: Player,
        main_character: Character,
        superhero: Character,
        scene_manager: SceneManager,
        save: Save,
        end: End
    ) -> None:
        """
        These variables are used when preparing the scenes, so make sure the
        name of the variable matches the story scenes when necessary i.e.
        [prize] [superhero] etc. (exception made for character classes!)
        """
        self.player = player
        self.scenes = import_json('story/scenes.json', 'scenes')
        self.main_character = main_character
        self.superhero = superhero
        self.scene_manager = scene_manager
        self.save = save
        self.end = end
        self.pints = 9
        self.won = False
        self.prize = get_random_beer()
        self.insult = random_insult()

    def update_main_character(self, character: Character) -> None:
        self.main_character = character

    def update_superhero(self, superhero: Character) -> None:
        self.superhero = superhero

    def get_pints(self) -> int:
        return self.pints

    def get_player_id(self) -> int:
        return self.player.id

    def get_character_name(self) -> str:
        return self.main_character.getName()

    def get_win(self) -> bool:
        return self.won

    def victory(self) -> None:
        self.won = True

    def update_pints(self, amount: int) -> int:
        new_pints = self.pints + amount
        if new_pints <= 0:
            print('Oh no! No more pints are in your system!')
            self.pints = 0
            return 0
        self.pints = new_pints
        print('Current pints: ', self.pints)
        return self.pints

    def start_game(self):
        scenario = 'introScene'
        while scenario != 'end_scene':
            try:
                scenario = self.scene_manager.manage(
                    Scene(
                        self.scenes[scenario]
                    ),
                    self
                )
            except Exception as e:
                print('Sorry, something went wrong')
                print('Error: ', e)

    def save_game(self):
        self.save.save(
            self.player.id,
            self.main_character.getName(),
            self.won,
            self.pints
        )

    def end_game(self):
        self.end.end(self.player)

    def run(self):
        self.start_game()
        self.save_game()
        self.end_game()
