from unittest import TestCase, main, mock
from game_engine.character import Character
from utils.fight import FightClub
from tests.unit.game_engine_tests.helper import dummy_character_request, dummy_character_request_win_stats


class TestFightClub(TestCase):

    def test_main_char_wins_speed(self):
        fight_club = FightClub(
            Character(dummy_character_request),
            Character(dummy_character_request_win_stats)
        )
        self.assertTrue(fight_club.round1_speed())

    '''
    Note for Helen, since we didn't have the time to implement the fight code
    testing wasn't completed for the fight code.
    I was unable to get the mock to work so time.sleep wouldn't run, which 
    slows the tests considerably, so I took out a lot of the fight code tests.
    '''

    # @mock.patch('time.sleep', return_value=None)
    def test_r2_main_char_win_intelligence(self):
        fight_club = FightClub(
            Character(dummy_character_request),
            Character(dummy_character_request_win_stats)
        )
        self.assertTrue(fight_club.round2_intelligence())


if __name__ == '__main__':
    main()
