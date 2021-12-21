from unittest import TestCase, main
from unittest.mock import patch

from game_engine.character.character import Character
from game_engine.game.game import Game
from save.player import Player
from save.db_connection import Query
from tests.unit.game_engine_tests.dummy_data import dummy_character_request


class GameTestCase(TestCase):
    def test_update_character(self):
        game_class = Game(
            Character(dummy_character_request),
            Character(dummy_character_request),
            Player(Query(), 'lou')
        )
        game_class.update_main_character('David')
        self.assertEqual('David', game_class.main_character)

    def test_get_pints_returns_num(self):
        game_class = Game(
            Character(dummy_character_request),
            Character(dummy_character_request),
            Player(Query(), 'lou')
        )
        result = game_class.get_pints()
        self.assertEqual(9, result)

    @patch('random.random')
    def test_get_random_beer_random_choice_called(self, mock_random):
        game_class = Game(
            Character(dummy_character_request),
            Character(dummy_character_request),
            Player(Query(), 'lou')
        )
        game_class.get_random_beer()
        self.assertTrue(1, mock_random.choice.call_count)


if __name__ == '__main__':
    main()
