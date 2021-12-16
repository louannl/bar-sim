from unittest import TestCase, main
from game_engine.game import Game


class GameTestCase(TestCase):
    def test_update_character(self):
        game_class = Game()
        game_class.update_main_character('David')
        self.assertEqual('David', game_class.main_character)

    def test_update_character_with_int(self):
        game_class = Game()
        game_class.update_main_character(123)
        self.assertEqual('123', game_class.main_character)


if __name__ == '__main__':
    main()
