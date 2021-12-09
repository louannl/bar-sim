from unittest import main, TestCase

from utils import DiceDecider


class DiceDeciderTestCase(TestCase):

    def test_dice_roll_int(self):
        test_roll_return = DiceDecider()
        result = test_roll_return.dice_roll()
        self.assertTrue(0 < result <= 6)

    def test_even_is_true(self):
        test_even = DiceDecider()
        result = test_even.is_even(2)
        self.assertTrue(result)
        result = test_even.is_even(4)
        self.assertTrue(result)
        result = test_even.is_even(6)
        self.assertTrue(result)

    def test_even_is_false(self):
        test_even_false = DiceDecider()
        result = test_even_false.is_even(1)
        self.assertFalse(result)
        result = test_even_false.is_even(3)
        self.assertFalse(result)
        result = test_even_false.is_even(5)
        self.assertFalse(result)

    def test_pint_increase_decider(self):
        test_decider = DiceDecider()
        result = test_decider.pint_increase_decider(1)
        self.assertEqual(1, result)
        result = test_decider.pint_increase_decider(2)
        self.assertEqual(1, result)
        result = test_decider.pint_increase_decider(3)
        self.assertEqual(2, result)
        result = test_decider.pint_increase_decider(4)
        self.assertEqual(2, result)
        result = test_decider.pint_increase_decider(5)
        self.assertEqual(3, result)
        result = test_decider.pint_increase_decider(6)
        self.assertEqual(3, result)


if __name__ == '__main__':
    main()
