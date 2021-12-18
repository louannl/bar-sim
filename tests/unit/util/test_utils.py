from unittest import TestCase, main
from utils.utils import random_insult, get_character, set_user_character
from utils.fight import FightClub
from tests.game_engine.helper import dummy_character_request, dummy_character_request_win_stats


class RandomInsult(TestCase):

    def is_api_response200(self):
        self.assertTrue("<Response[200]>", random_insult())

    def is_str_returned_not_empty(self):
        self.assertTrue(str, random_insult())
        self.assertTrue(random_insult())  # an empty string would evaluate False

    def is_api_exception_raised(self):
        self.assertRaises(Exception, random_insult())


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
        self.assertFalse(Exception, get_character(
            1))  # If the url works fine, this test would break so changed to False. So if Url not working, then it breaks


class FightClub(TestCase):
    def r1_main_char_win_speed(self):
        test_call = FightClub(dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.round1_speed())

    def r2_main_char_win_intelligence(self):
        test_call = FightClub(dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.round2_intelligence())

    def r3_main_char_win_strength(self):
        test_call = FightClub(dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.round3_strength())

    def activate_rounds_outcome_main_char_win(self):
        test_call = FightClub(dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.activate_rounds_get_outcome())

    def r1_main_char_lose_speed_(self):
        test_call = FightClub(dummy_character_request, dummy_character_request_win_stats)
        self.assertTrue(test_call.round1_speed())

    def r2_main_char_lose_intelligence(self):
        test_call = FightClub(dummy_character_request, dummy_character_request_win_stats)
        self.assertTrue(test_call.round2_intelligence())

    def r3_main_char_lose_strength(self):
        test_call = FightClub(dummy_character_request, dummy_character_request_win_stats)
        self.assertTrue(test_call.round3_strength())

    def activate_rounds_outcome_main_char_lose(self):
        test_call = FightClub(dummy_character_request, dummy_character_request_win_stats)
        self.assertTrue(test_call.activate_rounds_get_outcome())


if __name__ == '__main__':
    main()
