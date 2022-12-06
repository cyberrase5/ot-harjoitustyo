from database_connection import get_database_connection
from session import session

class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_course(self, name, ects, degree_id, mandatory):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO courses (course_name, ects, degree_id, mandatory) VALUES (?, ?, ?, ?)", [name, ects, degree_id, mandatory])

    def add_enrollment(self, user_id, course_id):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO participants (user_id, course_id, grade) VALUES (?, ?, -1)", [user_id, course_id])

        self._connection.commit()

    def get_mandatory_courses_id(self, degree_id):

        cursor = self._connection.cursor()

        cursor.execute("SELECT rowid FROM courses WHERE degree_id=? AND mandatory=1", [degree_id])

        ret = cursor.fetchall()

        return ret

    def create_mandatory_enrollments_id(self, user_id, degree_id):
        courses = self.get_mandatory_courses_id(degree_id)

        for course in courses:
            self.add_enrollment(user_id, course[0])


    def get_course_data_mainpage(self):
        cursor = self._connection.cursor()

        sql = "SELECT C.course_name, P.grade FROM courses C, participants P, users U WHERE C.rowid=P.course_id AND P.user_id=U.rowid AND U.rowid=?"

        cursor.execute(sql, [session._user_id])

        result = cursor.fetchall()

        return result

    def get_user_id_and_degree_id(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT rowid, degree_id FROM users WHERE username=?", [username])

        return cursor.fetchone()


course_repository = CourseRepository(get_database_connection())