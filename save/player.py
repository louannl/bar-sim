from save.query import Query


# Composition over inheritance
class Player:
    def __init__(self, query: Query) -> None:
        self.query = query

    def check_player(self, player_name: str) -> list:
        query_string = '''SELECT * FROM player WHERE full_name = %s'''
        query_result = self.query.db_connect(query_string, [(player_name)])
        return query_result

    def create_player(self, player_name: str):
        query_string = '''INSERT INTO player (full_name) VALUES (%s);'''
        query_result = self.query.db_connect(query_string, [(player_name)])
        return query_result
