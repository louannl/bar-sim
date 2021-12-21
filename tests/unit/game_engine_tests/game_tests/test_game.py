from unittest import TestCase, main

from game_engine.game.pints_counter import PintCounter


class PintCounterTest(TestCase):
    def test_get_pints_returns_starting_pints(self):
        pint_counter = PintCounter()
        result = pint_counter.get_pints()
        self.assertEqual(9, result)


if __name__ == '__main__':
    main()
