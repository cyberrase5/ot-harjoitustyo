import os
import sqlite3

dirname = os.path.dirname(__file__)

db_connection = sqlite3.connect("database.db")
db_connection.row_factory = sqlite3.Row


def get_database_connection():
    return db_connection


def test_connection():
    db_connection = sqlite3.connect("tests.db")
    db_connection.row_factory = sqlite3.Row

    return db_connection
