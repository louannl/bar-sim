from save.connection import connect_db


class Query:
    def __init__(self):
        pass

    def db_connect(self, db_query: str, params: list):
        db_connection = {}
        try:
            db_connection = connect_db()
            cursor = db_connection.cursor()
            cursor.execute(db_query, params)
            result = cursor.fetchall()
            cursor.close()
            db_connection.commit()
        except Exception as error:
            print(error)
            raise error
        finally:
            if db_connection:
                db_connection.close()
        return result



