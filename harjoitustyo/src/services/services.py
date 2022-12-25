'''Called by GUI, calls repositories'''
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
        '''
        Includes logged in user's id and degree id
        '''

        self.user_repository = user_repository
        self.course_repository = course_repository

        self.user_id = None
        self.degree_id = None

    def update_logged_in_ids(self, user_id, degree_id):
        '''
        Called when logging in succesfully, updates user and degree id
        in sisu_services object
        '''

        self.user_id = user_id
        self.degree_id = degree_id

    def get_user_id_and_degree_id(self, username):
        '''
        Calls repository's function, gets user and degree ids based on username
        RETURNS tuple of user_id, degree_id
        '''

        ids = user_repository.get_user_id_and_degree_id(username)

        return ids

    def authenticate_login(self, username, password):
        '''
        Calls repository's function, and if it returns false,
        RAISES InvalidCredentialError
        '''

        if not user_repository.authenticate_login(username, password):
            raise InvalidCredentialsError

    def register(self, username, password, degree_id):
        '''
        Calls repository's function, and if it returns false,
        RAISES UsernameInUseError, also calls CourseRepository's
        mandatory enrollment creation function. Called when registrating
        '''

        if not user_repository.add_user(username, password, degree_id):
            raise UsernameInUseError

        # add mandatory enrollments

        user_id = user_repository.get_user_id_and_degree_id(username)

        course_repository.create_mandatory_enrollments_id(user_id[0], degree_id)


    def calculate_gpa(self, user_id):
        '''
        Calls repository's function,
        calculates gpa of completed (grade != -1) courses
        RETURNS gpa as number
        '''

        user_gpa = course_repository.calculate_GPA(user_id)

        return user_gpa


    def total_ects_in_curriculum(self, user_id):
        '''
        Calls repository's function,
        calculates sum of all ects in user's curriculum
        RETURNS sum as number
        '''

        ects = course_repository.total_ects_in_curriculum(user_id)

        return ects


    def completed_ects(self, user_id):
        '''
        Calls repository's function,
        calculates sum of completed courses' (grade != -1) ects
        RETURNS sum as number
        '''

        ects = course_repository.completed_ects(user_id)

        return ects


    def get_course_data_mainpage(self, user_id):
        '''
        Calls repository's function, gets list of user's courses,
        including course name, id, grade,
        RETURNS the list (parsed elsewhere)
        '''

        return course_repository.get_course_data_mainpage(user_id)


    def update_grade(self, course_id, user_id, grade):
        '''
        Calls repository's function, updates user's grade in a course.
        RAISES InvalidGradeError if grade not between 0 and 5
        '''

        if not 0 <= int(grade) <= 5:
            raise InvalidGradeError

        course_repository.update_grade(course_id, user_id, grade)


    def add_course_to_curriculum(self, course_name, ects, degree_id, user_id):
        '''
        Calls repository's function,
        RAISES NegativeEctsError if ects are negative (no such course)
        '''

        ret_value = course_repository.add_course_to_curriculum(course_name, ects, degree_id, user_id)

        if ret_value == -1:
            raise NegativeEctsError


    def delete_enrollment(self, user_id, del_id):
        '''
        Calls repository's function
        '''

        course_repository.delete_enrollment(user_id, del_id)


    def users_size(self):

        return user_repository.users_size()


sisu_service = SisuService()
