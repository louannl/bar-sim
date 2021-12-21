from unittest import TestCase, main
from unittest.mock import patch
from utils.utils import get_random_beer


class TestRandomBeer(TestCase):
    @patch('random.random')
    def test_get_random_beer_random_choice_called(self, mock_random):
        get_random_beer()
        self.assertTrue(1, mock_random.choice.call_count)


if __name__ == '__main__':
    main()
