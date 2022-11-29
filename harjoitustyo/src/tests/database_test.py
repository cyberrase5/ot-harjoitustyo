import unittest
from UserRepository import user_repository
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

        
