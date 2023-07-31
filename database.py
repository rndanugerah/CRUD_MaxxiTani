import mysql.connector
from config import DATABASE_CONFIG

def create_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)
