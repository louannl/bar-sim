from unittest import TestCase, main
from game_engine.character.character import Character
from game_engine.game import Game
from tests.unit.game_engine_tests.dummy_data import dummy_character_request


class GameTestCase(TestCase):
    def test_update_character(self):
        game_class = Game(Character(dummy_character_request),
                          Character(dummy_character_request))
        game_class.update_main_character('David')
        self.assertEqual('David', game_class.main_character)

    def test_get_pints_returns_num(self):
        game_class = Game(Character(dummy_character_request),
                          Character(dummy_character_request))
        result = game_class.get_pints()
        self.assertEqual(9, result)


if __name__ == '__main__':
    main()
