from unittest import TestCase, main
from tests.unit.game_engine_tests.helper import dummy_character_request, dummy_character_request_win_stats


class FightClub(TestCase):
    def r1_main_char_win_speed(self):
        test_call = FightClub(
            dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.round1_speed())

    def r2_main_char_win_intelligence(self):
        test_call = FightClub(
            dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.round2_intelligence())

    def r3_main_char_win_strength(self):
        test_call = FightClub(
            dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.round3_strength())

    def activate_rounds_outcome_main_char_win(self):
        test_call = FightClub(
            dummy_character_request_win_stats, dummy_character_request)
        self.assertTrue(test_call.activate_rounds_get_outcome())

    def r1_main_char_lose_speed_(self):
        test_call = FightClub(dummy_character_request,
                              dummy_character_request_win_stats)
        self.assertTrue(test_call.round1_speed())

    def r2_main_char_lose_intelligence(self):
        test_call = FightClub(dummy_character_request,
                              dummy_character_request_win_stats)
        self.assertTrue(test_call.round2_intelligence())

    def r3_main_char_lose_strength(self):
        test_call = FightClub(dummy_character_request,
                              dummy_character_request_win_stats)
        self.assertTrue(test_call.round3_strength())

    def activate_rounds_outcome_main_char_lose(self):
        test_call = FightClub(dummy_character_request,
                              dummy_character_request_win_stats)
        self.assertTrue(test_call.activate_rounds_get_outcome())


if __name__ == '__main__':
    main()
