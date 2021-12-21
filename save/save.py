from datetime import datetime
from save.db_connection import DBConnection


class Save:
    def __init__(self, db: DBConnection) -> None:
        self.db = db

    def save(self, player_id: int, character: str, won: bool, pint_count: int):
        return self.db.query(
            '''
            INSERT INTO game (player_id, player_character, won, pint_count,
            game_date)
            VALUES (%s, %s, %s, %s, %s)
            ''',
            [
                player_id,
                character,
                won,
                pint_count,
                datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            ]
        )
