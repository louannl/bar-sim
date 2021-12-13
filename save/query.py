from save.connection import connect_db, GameDBConnection


class Query:
    def __init__(self):
        pass

    def db_connect(self, db_query: str, params: list):
        db_connection = {}
        try:
            db_connection = connect_db()
            cursor = db_connection.cursor()
            cursor.execute(db_query, params)
            result = cursor.fetchall()
            cursor.close()
            db_connection.commit()
        except Exception:
            raise GameDBConnection('Information not available!')
        finally:
            if db_connection:
                db_connection.close()
        return result

    # parameterization of the SQL queries helps protect against SQL injection
    # def check_result(self, query_result, player_name):
    #     if query_result == 0:
    #         self.send_player_data(player_name)
    #     return query_result

    def get_id(self, player_name):
        query_string = ('''INSERT INTO game (player_id)
        SELECT id
        FROM  player
        WHERE full_name = %s ''')
        params = (player_name,)
        send_get_id_connect = self.db_connect(query_string, params)
        return send_get_id_connect

    def insert_game(self, player_name, character_name, end_result, game_time_string):
        query_string = '''UPDATE game 
        SET name = %s, main_character = %s, result = %s, date = %s
        ORDER BY id DESC
        LIMIT 1'''
        params = (player_name, character_name, end_result, game_time_string,)
        send_game_connection = self.db_connect(query_string, params)
        return send_game_connection

    def update_total_plays(self, player_name):
        query_string = '''UPDATE player p
        INNER JOIN (SELECT player_id, COUNT(player_id) as player_count 
        FROM game 
        GROUP BY player_id) AS g
        ON g.player_id = p.id
        SET p.total_plays = g.player_count
        WHERE full_name = %s'''
        params = (player_name,)
        update_total_play = self.db_connect(query_string, params)
        return update_total_play
