from save.connection import connect_db
from prettytable import from_db_cursor


class DBConnection:
    def __init__(self):
        self.db_connection = connect_db()

    def query(self, db_query: str, params: list):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(db_query, params)
            result = cursor.fetchall()
            cursor.close()
            self.db_connection.commit()
        except Exception as error:
            print(error)
            raise error
        return result

    def query_table(self, db_query: str):
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(db_query)
            result = from_db_cursor(cursor)
            cursor.close()
            self.db_connection.commit()
        except Exception as error:
            print(error)
            raise error
        return result
