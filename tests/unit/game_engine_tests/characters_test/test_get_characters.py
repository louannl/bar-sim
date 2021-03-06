import os
from dotenv import load_dotenv
from unittest import TestCase, main
from unittest.mock import patch

from game_engine.character.get_characters import (
    get_character,
    get_random_superhero,
    set_user_character
)
from utils.custom_exceptions import ApiError
from tests.unit.utils_tests.helper import player_options, superhero_list

load_dotenv()


class TestGetCharacter(TestCase):
    def test_is_success(self):
        result = get_character(1)
        self.assertEqual("success", result['response'])

    def test_get_character_raises_error_invalid_string(self):
        with self.assertRaises(ApiError):
            get_character('four')

    @patch.dict(os.environ, {"SUPERHERO_API_KEY": "NOT_A_VALID_KEY"})
    def test_invalid_api_key(self):
        with self.assertRaises(ApiError):
            get_character(1)


class TestRandomSuperhero(TestCase):
    @patch('random.random')
    def test_get_random_superhero_random_choice_called(self, mock_random):
        get_random_superhero(superhero_list)
        self.assertTrue(1, mock_random.choice.call_count)


class TestSetUserCharacter(TestCase):
    @patch('game_engine.character.get_characters.input')
    def test_set_user_character_selects_first_option(self, mock_input):
        mock_input.side_effect = iter(['y'])
        result = set_user_character(player_options)
        self.assertEqual(result, 140)

    @patch('game_engine.character.get_characters.input')
    def test_set_user_character_selects_final_option(self, mock_input):
        mock_input.side_effect = iter(['n', 'n', 'n', 'y'])
        result = set_user_character(player_options)
        self.assertEqual(result, 540)

    @patch('game_engine.character.get_characters.input')
    def test_set_user_character_exits_game_after_browse_all_options(
        self,
        mock_input
    ):
        with self.assertRaises(SystemExit):
            mock_input.side_effect = iter(['n', 'n', 'n', 'n', ' '])
            self.assertRaises(SystemExit, set_user_character(player_options))


if __name__ == '__main__':
    main()
