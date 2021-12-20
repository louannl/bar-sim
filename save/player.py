from save.query import Query


class Player:
    def __init__(self, query: Query, name: str) -> None:
        self.query = query
        self.name = name
        self.id = None
        self.create_or_return_id()

    def exists(self) -> list:
        query_string = '''SELECT * FROM player WHERE full_name = %s'''
        query_result = self.query.db_connect(
            query_string, [(self.name)])
        return query_result

    def create(self):
        query_string = '''INSERT INTO player (full_name) VALUES (%s);'''
        query_result = self.query.db_connect(
            query_string, [(self.name)])
        return query_result

    def create_or_return_id(self) -> None:
        if self.id:
            return
        player_exists = self.exists()
        if not player_exists:
            self.create()
            player_exists = self.exists()

        self.id = player_exists[0][0]
