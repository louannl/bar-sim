from save.query import Query


# Composition over inheritance
class CheckPlayer:
    def __init__(self, query: Query) -> None:
        self.query = query

    def check_player(self, player_name: str) -> list:
        query_string = '''SELECT * FROM player WHERE full_name = %s'''
        query_result = self.query.db_connect(query_string, [(player_name)])
        return query_result


class CreatePlayer:
    def __init__(self, query: Query) -> None:
        self.query = query

    # TODO: Was called send_player_data
    def create_player(self, player_name: str):
        query_string = '''INSERT INTO player (full_name) VALUES (%s);'''
        query_result = self.query.db_connect(query_string, [(player_name)])
        # TODO: Does this actually return a value???
        return query_result

