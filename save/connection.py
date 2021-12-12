import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        auth_plugin='mysql_native_password',
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT')
    )


class GameDBConnection(Exception):
    pass
