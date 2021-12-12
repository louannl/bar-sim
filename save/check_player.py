from save.query import Query


# Composition over inheritance
class CheckPlayer:
    def __init__(self, query: Query) -> None:
        self.query = query

    def check_player(self, player_name: str):
        query_string = '''SELECT * FROM player WHERE full_name = %s'''
        params = (player_name)
        query_result = self.query.game_db_query(query_string, [params])
        return query_result
