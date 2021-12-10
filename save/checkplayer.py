from save.dbquery import Query
from save.connection import connect_db, GameDBConnection

class CheckPlayer(Query):
    def game_db_query(self, db_query, params):
        db_connection = {}
        try:
            db_connection = connect_db()
            cursor = db_connection.cursor()
            cursor.execute(db_query, params)
            results = cursor.fetchall()
            len_results = (len(results))
            cursor.close()
            db_connection.commit()
        except Exception:
            raise GameDBConnection('Information not available!')
        finally:
            if db_connection:
                db_connection.close()
        return len_results

    def check_player(self, player_name):
        query_string = '''SELECT * FROM player WHERE Full_Name = %s'''
        params = (player_name,)
        query_result = (self.game_db_query(query_string, params))
        return query_result