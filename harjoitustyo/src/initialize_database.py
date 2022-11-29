from database_connection import get_database_connection, test_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, degree_id INTEGER)")

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

def initialize_database_test():
    connection = test_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()