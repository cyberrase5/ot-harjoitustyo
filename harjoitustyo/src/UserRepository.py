from database_connection import get_database_connection
from CourseRepository import course_repository


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, username, password, degree):
        cursor = self._connection.cursor()

        try:
            cursor.execute(
                "INSERT INTO users \
                    (username, password, degree_id) VALUES (?, ?, ?)", (username, password, degree))
        except:
            print("Error")
            self._connection.commit() # dumb but too slow otherwise
            return

        self._connection.commit()

        # enroll on mandatory courses
        user_id = cursor.execute("SELECT rowid FROM users WHERE username=?", [username])
        user_id = user_id.fetchone()[0]
        course_repository.create_mandatory_enrollments_id(user_id, degree)


    def users_size(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")

        ret = cursor.fetchone()[0]

        return ret

    def authenticate_login(self, username, password):
        cursor = self._connection.cursor()

        cursor.execute("SELECT 1 FROM users WHERE username=? AND password=?", [username, password])
        ret = cursor.fetchone()

        if ret:
            return True

        return False

    def update_grade(self):
        cursor = self._connection.cursor()
    

user_repository = UserRepository(get_database_connection())
