from unittest import TestCase, main
from game_engine.game.insult import Insult


class TestRandomInsult(TestCase):
    def test_random_insult_returns_value(self):
        result = Insult().get_random_insult()
        # AssertTrue will also check that it does not return an empty string
        self.assertTrue(result)
    '''
    Old tests used to random insult api which was used, but removed later
    due to very 'inappropriate' insults.

    Kept in comment block, as to my knowledge, this is still being marked.

    def test_random_insult_fails_url(self):
        insult = Insult()
        insult.url = 'invalid_url'
        with self.assertRaises(Exception):
            insult.get_random_insult()

    @patch('requests.get')
    def test_random_insult_returns_json_dict_insult_value(self, mock_request):
        mock_request.return_value.json.return_value = {
            "insult": "insult_string"}
        json_data = Insult().get_random_insult()
        self.assertEqual(json_data, "insult_string")

    @patch('requests.get')
    def test_random_insult_raises_error(self, mock_request):
        mock_response = MagicMock
        mock_response.side_effect = requests.exceptions.ConnectionError()
        mock_request.return_value = mock_response
        result = Insult().get_random_insult()
        self.assertRaises(Exception, result)
        self.assertIsNone(result)
    '''


if __name__ == '__main__':
    main()
