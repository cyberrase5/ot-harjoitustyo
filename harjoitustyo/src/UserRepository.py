from database_connection import get_database_connection

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, username, password, degree):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO users (username, password, degree_id) VALUES (?, ?, ?)", (username, password, degree))

        self._connection.commit()

    def users_size(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")

        ret = cursor.fetchone()[0]

        return ret

user_repository = UserRepository(get_database_connection())
