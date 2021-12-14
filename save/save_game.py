from datetime import datetime
from save.query import Query


class CreateGame:
    def __init__(self, query: Query) -> None:
        self.query = query

    def create_game_save(self, player_id: int, character: str, won: bool):
        game_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query_string = '''
        INSERT INTO game (player_id, player_character, won, game_date)
        VALUES (%s, %s, %s, %s)
        '''
        send_game_connection = self.query.db_connect(
            query_string, [player_id, character, won, game_date])
        return send_game_connection


class UpdateGame:
    def __init__(self, query: Query) -> None:
        self.query = query

    def update_game_save(self, player_id: int):
        query_string = '''
        UPDATE player
        SET total_plays = total_plays + 1
        WHERE id = %s;
        '''
        send_game_connection = self.query.db_connect(
            query_string, [player_id])
        return send_game_connection
