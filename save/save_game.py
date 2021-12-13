from datetime import datetime
from save.query import Query


class SaveGame:
    def save_game(self):
        self.game_time = datetime.now()
        return self.game_time

    def convert_timestamp(self):
        game_time_string = self.game_time.strftime('%d-%m-%Y')
        return game_time_string

    def save(self):
        self.save_game()
        gts = self.convert_timestamp()
        return gts


class CreateGame:
    def __init__(self, query: Query) -> None:
        self.query = query

    def create_game_save(self, player_id: int, character: str, won: bool):
        game_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print('date: ', game_date)

        query_string = '''
        INSERT INTO game (player_id, player_character, won, game_date)
        VALUES (%s, %s, %s, %s)
        '''
        send_game_connection = self.query.db_connect(
            query_string, [player_id, character, won, game_date])
        return send_game_connection
