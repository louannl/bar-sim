import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    con = mysql.connector.connect(
        host = os.getenv('HOST'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'),
        auth_plugin = os.getenv('AUTH_PLUGIN'),
        database = os.getenv('DATABASE')
    )
    return con


