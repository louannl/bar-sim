from save.db_connection import DBConnection


class Player:
    def __init__(self, db: DBConnection, name: str) -> None:
        self.db = db
        self.name = name
        self.id = None
        self.create_or_return_id()

    def exists(self) -> list:
        return self.db.query(
            '''SELECT * FROM player WHERE full_name = %s''',
            [(self.name)]
        )

    def create(self) -> None:
        self.db.query(
            '''INSERT INTO player (full_name) VALUES (%s);''',
            [(self.name)]
        )

    def create_or_return_id(self) -> None:
        if self.id:
            return
        player = self.exists()
        if not player:
            self.create()
            player = self.exists()

        self.id = player[0][0]
