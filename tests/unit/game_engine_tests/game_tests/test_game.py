from unittest import TestCase, main
from unittest.mock import patch

from game_engine.character.character import Character
from game_engine.game.game import Game
from game_engine.game.pints_counter import PintCounter
from game_engine.scene.scene_manager import SceneManager
from save.end import End
from save.player import Player
from save.db_connection import DBConnection
from save.save import Save
from save.stats import Stats
from tests.unit.game_engine_tests.dummy_data import (
    dummy_character_request, dummy_character_request_win_stats)


class GameTestCase(TestCase):
    def test_update_character(self):
        db = DBConnection()
        game_class = Game(
            Player(db, 'Thomas the Tank Engine'),
            Character(dummy_character_request),
            Character(dummy_character_request),
            SceneManager(),
            PintCounter(),
            Save(db),
            End(Stats(db))
        )
        game_class.update_main_character(dummy_character_request_win_stats)
        self.assertEqual(
            dummy_character_request_win_stats,
            game_class.main_character
        )

    @patch('random.random')
    def test_get_random_beer_random_choice_called(self, mock_random):
        db = DBConnection()
        game_class = Game(
            Player(db, 'Thomas the Tank Engine'),
            Character(dummy_character_request),
            Character(dummy_character_request),
            SceneManager(),
            PintCounter(),
            Save(db),
            End(Stats(db))
        )
        game_class.get_random_beer()
        self.assertTrue(1, mock_random.choice.call_count)

    def test_get_pints_returns_starting_pints(self):
        pint_counter = PintCounter()
        result = pint_counter.get_pints()
        self.assertEqual(9, result)


if __name__ == '__main__':
    main()
