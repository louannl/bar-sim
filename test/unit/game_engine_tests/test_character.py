from unittest import TestCase, main
from game_engine.character import Character
from test.unit.game_engine_tests.helper import dummy_character_request


class CharacterTestCase(TestCase):
    def test_get_name(self):
        character_class = Character(dummy_character_request)
        result = character_class.getName()
        self.assertEqual('A-Bomb', result)


if __name__ == '__main__':
    main()
