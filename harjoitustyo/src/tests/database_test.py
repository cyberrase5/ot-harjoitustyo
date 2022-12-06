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

        
