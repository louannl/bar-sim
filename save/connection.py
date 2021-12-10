import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    con = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        auth_plugin=os.getenv('DB_AUTH_PLUGIN'),
        database=os.getenv('DB_NAME')
    )
    return con

class GameDBConnection(Exception):
    pass