import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect("testi.db")
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection