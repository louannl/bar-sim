from save.db_connection import DBConnection


class Stats:
    def __init__(self, db: DBConnection) -> None:
        self.db = db

    def return_play_count_and_win_count(self, player_id: int) -> list:
        return self.db.query(
            '''
            SELECT count(case when won = 1 then 1 end), count(*)
            FROM game
            WHERE player_id = %s
            ''',
            [(player_id)]
        )[0]

    def display_leaderboard(self):
        return self.db.query_table(
            '''
            SELECT p.full_name AS player, sum(pint_count) AS pint_total
            FROM game AS g
            JOIN player AS p on p.id = g.player_id
            GROUP BY 1
            ORDER BY 2 desc
            LIMIT 3;
            '''
        )
