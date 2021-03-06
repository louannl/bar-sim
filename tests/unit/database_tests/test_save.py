from unittest import TestCase, main
from unittest.mock import patch, MagicMock
import save.db_connection
from save.db_connection import DBConnection


@patch('save.db_connection.connect_db')
class MyTestCase(TestCase):

    def test_connection_patch(self, connect_db):
        self.assertIs(save.db_connection.connect_db, connect_db)

    def test_check_player_query(self, connect_db):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        cursor = mock_conn.cursor.return_value
        query_obj = DBConnection()
        player_name = 'player name'
        query = '''SELECT * FROM player WHERE full_name = %s'''
        query_obj.query(query, [player_name])

        cursor.execute.assert_called_with(query, [player_name])
        self.assertEqual(1, cursor.fetchall.call_count)
        self.assertEqual(1, mock_conn.commit.call_count)
        self.assertRaises(Exception, query_obj.query,
                          query, player_id=' ')

    def test_check_player_query_fails_with_incorrect_query_params(self, connect_db):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        query_obj = DBConnection()
        player_name = 'player name'
        query = '''SELECT * FROM player WHERE full_name = %s'''
        query_obj.query(query, [player_name])
        self.assertRaises(Exception, query_obj.query, query, player_id='3')

    def test_create_player_query(self, connect_db):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        cursor = mock_conn.cursor.return_value
        query_obj = DBConnection()
        player_name = 'player name'
        query = '''INSERT INTO player (full_name) VALUES (%s);'''
        query_obj.query(query, [player_name])

        cursor.execute.assert_called_with(query, [player_name])
        self.assertEqual(1, cursor.close.call_count)
        self.assertEqual(1, cursor.fetchall.call_count)
        self.assertEqual(1, mock_conn.commit.call_count)
        self.assertRaises(Exception, query_obj.query,
                          query, player_id=' ')

    def test_create_player_query_fails_with_incorrect_query_params(
        self,
        connect_db
    ):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        query_obj = DBConnection()
        player_name = 'player name'
        query = '''INSERT INTO player (full_name) VALUES (%s);'''
        query_obj.query(query, [player_name])
        self.assertRaises(Exception, query_obj.query, query, player_id='3')

    def test_return_play_count_and_win_count_query(self, connect_db):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        cursor = mock_conn.cursor.return_value
        query_obj = DBConnection()
        player_id = 'player_id'
        query = '''SELECT count(case when won = 1 then 1 end), count(*)
        FROM game
        WHERE player_id = %s'''
        query_obj.query(query, [player_id])

        cursor.execute.assert_called_with(query, [player_id])
        self.assertEqual(1, cursor.close.call_count)
        self.assertEqual(1, cursor.fetchall.call_count)
        self.assertEqual(1, mock_conn.commit.call_count)
        self.assertRaises(Exception, query_obj.query,
                          query, player_name=' ')

    def test_play_and_win_count_query_fails_with_incorrect_query_params(
        self,
        connect_db
    ):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        query_obj = DBConnection()
        player_id = 'player_id'
        query = '''SELECT count(case when won = 1 then 1 end), count(*)
        FROM game
        WHERE player_id = %s'''
        query_obj.query(query, [player_id])
        self.assertRaises(Exception, query_obj.query, query, player_name='3')

    def test_display_leaderboard_connection(self, connect_db):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        cursor = mock_conn.cursor.return_value
        query_obj = DBConnection()
        query = '''SELECT p.full_name AS player, sum(pint_count) AS pint_total
        FROM game AS g
        JOIN player AS p on p.id = g.player_id
        GROUP BY 1
        ORDER BY 2 desc
        LIMIT 3;'''
        query_obj.query_table(query)

        cursor.execute.assert_called_with(query)
        self.assertEqual(1, cursor.close.call_count)
        self.assertEqual(1, cursor.fetchall.call_count)
        self.assertEqual(1, mock_conn.commit.call_count)
        self.assertRaises(Exception, query_obj.query,
                          query, player_id=' ')

    def test_display_leaderboard_connection_fails_with_incorrect_params(
        self,
        connect_db
    ):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        query_obj = DBConnection()
        query = '''SELECT p.full_name AS player, sum(pint_count) AS pint_total
        FROM game AS g
        JOIN player AS p on p.id = g.player_id
        GROUP BY 1
        ORDER BY 2 desc
        LIMIT 3;'''
        query_obj.query_table(query)
        self.assertRaises(Exception, query_obj.query, query, player_id='3')

    @patch('prettytable.from_db_cursor')
    def test_display_leaderboard_from_db_cursor_called(
        self,
        connect_db,
        from_db_cursor
    ):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        query_obj = DBConnection()
        query = '''SELECT p.full_name AS player, sum(pint_count) AS pint_total
            FROM game AS g
            JOIN player AS p on p.id = g.player_id
            GROUP BY 1
            ORDER BY 2 desc
            LIMIT 3;'''
        query_obj.query_table(query)
        self.assertTrue(from_db_cursor.called)

    def test_create_game_save_query(self, connect_db):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        cursor = mock_conn.cursor.return_value
        query_obj = DBConnection()
        player_id, character, won, pint_count, game_date = 'player_id', 'char', 'Bool', 'count', 'time_stamp'
        params = [player_id, character, won, pint_count, game_date]
        query = '''
        INSERT INTO game (player_id, player_character, won, pint_count, game_date)
        VALUES (%s, %s, %s, %s, %s)
        '''
        query_obj.query(query, params)

        cursor.execute.assert_called_with(query, params)
        self.assertEqual(1, cursor.close.call_count)
        self.assertEqual(1, cursor.fetchall.call_count)
        self.assertEqual(1, mock_conn.commit.call_count)
        self.assertRaises(Exception, query_obj.query,
                          query, player_id=' ')

    def test_create_game_save_query_fails_with_too_few_query_params(
        self,
        connect_db
    ):
        mock_conn = MagicMock()
        connect_db.return_value = mock_conn
        query_obj = DBConnection()
        player_id, character, won, pint_count, game_date = 'player_id', 'char', 'Bool', 'count', 'time_stamp'
        params = [player_id, character, won, pint_count, game_date]
        query = '''
                INSERT INTO game (player_id, player_character, won, pint_count, game_date)
                VALUES (%s, %s, %s, %s, %s)
                '''
        query_obj.query(query, params)
        self.assertRaises(Exception, query_obj.query, query, player_id='3')


if __name__ == '__main__':
    main()
