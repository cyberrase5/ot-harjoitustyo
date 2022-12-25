from repositories.UserRepository import user_repository
from repositories.CourseRepository import course_repository

class InvalidCredentialsError(Exception):
    pass

class UsernameInUseError(Exception):
    pass

class InvalidGradeError(Exception):
    pass

class NegativeEctsError(Exception):
    pass


class SisuService:

    def __init__(self):

        self.user_repository = user_repository
        self.course_repository = course_repository

        self.user_id = None
        self.degree_id = None

    def update_logged_in_ids(self, user_id, degree_id):

        self.user_id = user_id
        self.degree_id = degree_id

    def get_user_id_and_degree_id(self, username):

        ids = user_repository.get_user_id_and_degree_id(username)

        return ids

    def authenticate_login(self, username, password):

        if not user_repository.authenticate_login(username, password):
            raise InvalidCredentialsError

    def register(self, username, password, degree_id):

        if not user_repository.add_user(username, password, degree_id):
            raise UsernameInUseError

        # add mandatory enrollments

        user_id = user_repository.get_user_id_and_degree_id(username)

        course_repository.create_mandatory_enrollments_id(user_id[0], degree_id)


    def calculate_gpa(self, user_id):

        user_gpa = course_repository.calculate_GPA(user_id)

        return user_gpa


    def total_ects_in_curriculum(self, user_id):

        ects = course_repository.total_ects_in_curriculum(user_id)

        return ects


    def completed_ects(self, user_id):

        ects = course_repository.completed_ects(user_id)

        return ects


    def get_course_data_mainpage(self, user_id):

        return course_repository.get_course_data_mainpage(user_id)


    def update_grade(self, course_id, user_id, grade):

        if not 0 <= int(grade) <= 5:
            raise InvalidGradeError

        course_repository.update_grade(course_id, user_id, grade)


    def add_course_to_curriculum(self, course_name, ects, degree_id, user_id):

        ret_value = course_repository.add_course_to_curriculum(course_name, ects, degree_id, user_id)

        if ret_value == -1:
            raise NegativeEctsError


    def delete_enrollment(self, user_id, del_id):

        course_repository.delete_enrollment(user_id, del_id)


    def users_size(self):

        return user_repository.users_size()


sisu_service = SisuService()
