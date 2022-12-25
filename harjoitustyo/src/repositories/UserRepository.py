from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, username, password, degree):
        '''
        Called in registration, checks that username doesn't already exist.
        Makes entries to table participants for all mandatory courses
        '''
        cursor = self._connection.cursor()

        try:
            cursor.execute(
                "INSERT INTO users \
                    (username, password, degree_id) VALUES (?, ?, ?)", (username, password, degree))
        except:
            print("Error")
            self._connection.commit() # dumb but too slow otherwise
            return False

        self._connection.commit()

        return True


    def users_size(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")

        ret = cursor.fetchone()[0]

        return ret

    def authenticate_login(self, username, password):
        '''
        Called when logging in, RETURNS whether username and password are correct
        '''
        cursor = self._connection.cursor()

        cursor.execute("SELECT 1 FROM users WHERE username=? AND password=?", [username, password])
        ret = cursor.fetchone()

        if ret:
            return True

        return False

    def get_user_id_and_degree_id(self, username):
        '''
        Gets user_id and degree_id of this username
        '''
        cursor = self._connection.cursor()

        cursor.execute("SELECT rowid, degree_id FROM users WHERE username=?", [username])

        return cursor.fetchone()

user_repository = UserRepository(get_database_connection())
