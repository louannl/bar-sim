from unittest import TestCase, main, mock
from game_engine.character.character import Character
from game_engine.character.fight import FightClub
from tests.unit.game_engine_tests.dummy_data import (
    dummy_character_request, dummy_character_request_win_stats
)


class TestFightClub(TestCase):

    def test_main_char_wins_speed(self):
        fight_club = FightClub(
            Character(dummy_character_request),
            Character(dummy_character_request_win_stats)
        )
        self.assertTrue(fight_club.round1_speed())

    @mock.patch('time.sleep')
    def test_main_char_wins_intelligence(self, mock_input):
        fight_club = FightClub(
            Character(dummy_character_request),
            Character(dummy_character_request_win_stats)
        )
        self.assertTrue(fight_club.round2_intelligence())


if __name__ == '__main__':
    main()
