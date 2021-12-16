from datetime import datetime
from save.query import Query


class CreateGame:
    def __init__(self, query: Query) -> None:
        self.query = query

    def create_game_save(self, player_id: int, character: str, won: bool, pint_count: int):
        game_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        query_string = '''
        INSERT INTO game (player_id, player_character, won, pint_count, game_date)
        VALUES (%s, %s, %s, %s, %s)
        '''
        send_game_connection = self.query.db_connect(
            query_string, [player_id, character, won, pint_count, game_date])
        return send_game_connection


class GetGameHistory:
    def __init__(self, query: Query) -> None:
        self.query = query

    # Use this for the end of the game You have won 0 games out of 3

    def return_play_count_and_win_count(self, player_id):
        query_string = '''SELECT count(case when won = 1 then 1 end), count(*)
        FROM game 
        WHERE player_id = %s'''
        win_and_play_count = self.query.db_connect(query_string, [(player_id)])
        return win_and_play_count
