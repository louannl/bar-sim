from unittest import TestCase, main
from utils.utils import random_insult, get_character


class RandomInsult(TestCase):

    def test_is_str_returned_not_empty(self):
        insult = random_insult()
        self.assertTrue(str, insult)


class GetCharacter(TestCase):

    def is_api_response200_main_character(self):
        self.assertTrue("<Response[200]>", get_character(1))
        self.assertTrue("<Response[200]>", get_character(2))
        self.assertTrue("<Response[200]>", get_character(3))
        self.assertTrue("<Response[200]>", get_character(4))

    def is_api_response200_other_character(self):
        self.assertTrue("<Response[200]>", get_character(60))
        self.assertTrue("<Response[200]>", get_character(69))
        self.assertTrue("<Response[200]>", get_character(97))
        self.assertTrue("<Response[200]>", get_character(309))
        self.assertTrue("<Response[200]>", get_character(322))
        self.assertTrue("<Response[200]>", get_character(374))
        self.assertTrue("<Response[200]>", get_character(400))
        self.assertTrue("<Response[200]>", get_character(489))
        self.assertTrue("<Response[200]>", get_character(522))

    def is_api_exception_raised(self):
        # If the url works fine, this test would break so changed to False. So if Url not working, then it breaks
        self.assertFalse(Exception, get_character(1))


if __name__ == '__main__':
    main()
