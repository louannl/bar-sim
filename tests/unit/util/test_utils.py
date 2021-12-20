import unittest
import requests.exceptions
from unittest.mock import MagicMock, patch
from utils.utils import random_insult, get_random_beer, get_random_superhero, get_character, set_user_character


class TestCase(unittest.TestCase):
    @patch('requests.get')
    def test_random_insult_returns_value(self, mock_request):
        mock_request.return_value.content = "mock content"
        response = random_insult()
        self.assertIsNotNone(response.content)

    @patch('requests.get')
    def test_random_insult_returns_json_dict_insult_value(self, mock_request):
        mock_request.return_value.json.return_value = {"insult": "insult_string"}
        json_data = random_insult()
        self.assertEqual(json_data, "insult_string")

    @patch('requests.get')
    def test_random_insult_raises_error(self, mock_request):
        mock_response = MagicMock
        mock_response.side_effect = requests.exceptions.ConnectionError()
        mock_request.return_value = mock_response
        res = random_insult()
        self.assertRaises(Exception, res)
        self.assertIsNone(res)

    @patch('random.random')
    def test_get_random_beer_random_choice_called(self, mock_random):
        get_random_beer()
        self.assertTrue(1, mock_random.choice.call_count)

    def test_get_character_pass_if_argument_is_int(self):
        response = get_character(4)
        self.assertTrue(response['response'] == 'success')

    def test_get_character_pass_if_argument_is_valid_string(self):
        response = get_character('4')
        self.assertTrue(response['response'] == 'success')

    def test_get_character_fails_if_invalid_string(self):
        response = get_character('four')
        self.assertTrue(response['response'] == 'error')

    @patch('random.random')
    def test_get_random_superhero_random_choice_called(self, mock_random):
        get_random_superhero()
        self.assertTrue(1, mock_random.choice.call_count)

    @patch('utils.utils.input')
    def test_set_user_character_selects_first_option(self, mock_input):
        mock_input.side_effect = iter(['y'])
        result = set_user_character()
        self.assertEqual(result, 140)

    @patch('utils.utils.input')
    def test_set_user_character_selects_final_option(self, mock_input):
        mock_input.side_effect = iter(['n', 'n', 'n', 'y'])
        result = set_user_character()
        self.assertEqual(result, 540)

    @patch('utils.utils.input')
    def test_set_user_character_exits_game_after_browse_all_options(self, mock_input):
        with self.assertRaises(SystemExit):
            mock_input.side_effect = iter(['n', 'n', 'n', 'n', ' '])
            self.assertRaises(SystemExit, set_user_character())


if __name__ == '__main__':
    unittest.main()
