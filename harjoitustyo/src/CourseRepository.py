from database_connection import get_database_connection
from session import session

class CourseRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_course(self, name, ects, degree_id, mandatory):
        cursor = self._connection.cursor()

        cursor.execute("INSERT INTO courses (course_name, ects, degree_id, mandatory) VALUES (?, ?, ?, ?)", [name, ects, degree_id, mandatory])

        self._connection.commit()

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

        sql = "SELECT C.course_name, P.grade, C.rowid FROM courses C, participants P, users U "\
            "WHERE C.rowid=P.course_id AND P.user_id=U.rowid AND U.rowid=? ORDER BY C.rowid ASC"

        cursor.execute(sql, [session._user_id])

        result = cursor.fetchall()

        return result

    def get_user_id_and_degree_id(self, username):
        cursor = self._connection.cursor()

        cursor.execute("SELECT rowid, degree_id FROM users WHERE username=?", [username])

        return cursor.fetchone()


    def course_exists(self, name, degree_id):

        cursor = self._connection.cursor()

        cursor.execute("SELECT 1 FROM courses WHERE course_name=? AND degree_id=?", [name, degree_id])

        if cursor.fetchone():
            return True

        return False

    def update_grade(self, course_id, user_id, grade):
        if 0 > int(grade) or int(grade) > 5:
            return

        cursor = self._connection.cursor()

        cursor.execute("UPDATE participants SET grade=? WHERE course_id=? AND user_id=?", [grade, course_id, user_id])

        self._connection.commit()

    def add_course_to_curriculum(self, course_name, ects, degree_id, user_id):
        '''
        Creates a course if it doesn't exist,
        adds entry to table participants with args
        '''

        if not self.course_exists(course_name, degree_id):
            self.add_course(course_name, ects, degree_id, 0)

        course_id = self.get_course_id(course_name, degree_id)

        if not self.already_enrolled(user_id, course_id):
            self.add_enrollment(user_id, course_id)


    def get_course_id(self, course_name, degree_id):
        cursor = self._connection.cursor()

        cursor.execute("SELECT rowid FROM courses WHERE course_name=? AND degree_id=?", [course_name, degree_id])

        return cursor.fetchone()[0]

    def delete_enrollment(self, user_id, course_id):
        cursor = self._connection.cursor()

        cursor.execute("DELETE FROM participants WHERE user_id=? AND course_id=?", [user_id, course_id])

        self._connection.commit()

    def already_enrolled(self, user_id, course_id):
        cursor = self._connection.cursor()

        cursor.execute("SELECT 1 FROM participants WHERE user_id=? AND course_id=?", [user_id, course_id])

        if cursor.fetchone():
            return True

        return False

    def calculate_GPA(self, user_id):
        cursor = self._connection.cursor()

        cursor.execute("SELECT SUM(C.ects * P.grade)/CAST(SUM(C.ects) AS REAL) "\
            "FROM participants P, courses C WHERE P.course_id=C.rowid AND P.user_id=? AND P.grade!=-1", [user_id])

        return cursor.fetchone()[0]

    def courses_size(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM courses")

        return cursor.fetchone()[0]

    def participants_size(self):
        cursor = self._connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM participants")

        return cursor.fetchone()[0]


    # t_ functions, only used for testing

    def t_enrollment_exists(self, user_id, course_id, grade):
        cursor = self._connection.cursor()

        cursor.execute("SELECT 1 FROM participants WHERE course_id=? AND user_id=? AND grade=?", [course_id, user_id, grade])

        if cursor.fetchone():
            return True

        return False


course_repository = CourseRepository(get_database_connection())