import mysql.connector
from config import dbPassword


def connect_db(DBname):
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = dbPassword,
        auth_plugin = 'my_sql_native_password',
        database = DBname
    )
    return con


