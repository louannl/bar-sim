import os
from unittest import TestCase, main, mock
from utils.utils import random_insult, get_character


class RandomInsult(TestCase):

    def test_is_str_returned_not_empty(self):
        insult = random_insult()
        self.assertTrue(str, insult)


class GetCharacter(TestCase):

    def test_is_success(self):
        result = get_character(1)
        self.assertEqual("success", result['response'])

    def test_character_doesnt_exist(self):
        result = get_character('sdfsd')
        self.assertEqual("error", result['response'])
        self.assertEqual("invalid id", result['error'])

    @mock.patch.dict(os.environ, {"SUPERHERO_API_KEY": "NOT_A_VALID_KEY"})
    def test_invalid_api_key(self):
        result = get_character(1)
        self.assertEqual("error", result['response'])
        self.assertEqual("access denied", result['error'])


if __name__ == '__main__':
    main()
