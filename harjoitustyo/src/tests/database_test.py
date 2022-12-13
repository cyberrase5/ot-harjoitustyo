import unittest
from UserRepository import user_repository
from CourseRepository import course_repository
from database_connection import test_connection
from initialize_database import initialize_database_test


class TestUserRepository(unittest.TestCase):
    
    def setUp(self):
        initialize_database_test()
        user_repository._connection = test_connection()


    def test_deleting_decreases_size(self):

        user_repository.add_user("asd", "moi123", 1)
        cursor = user_repository._connection.cursor()
        orgSize = user_repository.users_size()

        cursor.execute("DELETE FROM users WHERE username='asd'")

        user_repository._connection.commit()

        self.assertEqual(user_repository.users_size(), orgSize-1)


    def test_user_is_actually_added(self):

        cursor = user_repository._connection.cursor()
        user_repository.add_user("asd", "moi123", 1)

        cursor.execute("SELECT password FROM users WHERE username='asd' AND degree_id=1")

        self.assertEqual(cursor.fetchone()[0], "moi123")


    def test_unique_usernames(self):

        orgSize = user_repository.users_size()
        user_repository.add_user("asd", "moi123", 1)
        user_repository.add_user("asd", "moi123", 1)

        self.assertEqual(user_repository.users_size(), orgSize + 1)


    def test_authenticate_login_works(self):

        user_repository.add_user("asd", "moi123", 1)

        self.assertTrue(user_repository.authenticate_login("asd", "moi123"))
        self.assertFalse(user_repository.authenticate_login("kakka", "pissa"))


    def test_adding_compsci_mandatory_courses_works(self):

        # added in test database initialization
        self.assertTrue(course_repository.course_exists("Ohjelmoinnin perusteet", 1))
        self.assertTrue(course_repository.course_exists("Ohjelmoinnin jatkokurssi", 1))
        self.assertTrue(course_repository.course_exists("Johdatus tietojenkäsittelytieteeseen", 1))
        self.assertTrue(course_repository.course_exists("Tietokantojen perusteet", 1))
        self.assertTrue(course_repository.course_exists("Tietokoneen toiminta", 1))


    def test_add_course_to_curriculum_no_course_duplicates(self):
        courses_initial_size = course_repository.courses_size()

        course_repository.add_course_to_curriculum("JYM", 5, 1, 1)
        self.assertEqual(course_repository.courses_size(), courses_initial_size + 1)

        course_repository.add_course_to_curriculum("JYM", 5, 1, 2) # different user
        self.assertEqual(course_repository.courses_size(), courses_initial_size + 1)


    def test_add_course_to_curriculum_no_enrollment_duplicates(self):
        participants_initial_size = course_repository.participants_size()

        course_repository.add_course_to_curriculum("JYM", 5, 1, 1)
        self.assertEqual(course_repository.participants_size(), participants_initial_size + 1)

        course_repository.add_course_to_curriculum("JYM", 5, 1, 1) # same course, same user
        self.assertEqual(course_repository.participants_size(), participants_initial_size + 1)


    def test_update_grade_between_zero_five(self):

        course_repository.add_enrollment(1, 1) # Default grade is -1

        # Grade shouldn't have been changed
        course_repository.update_grade(1, 1, -5)
        self.assertTrue(course_repository.t_enrollment_exists(1, 1, -1))

        course_repository.update_grade(1, 1, 6)
        self.assertTrue(course_repository.t_enrollment_exists(1, 1, -1))