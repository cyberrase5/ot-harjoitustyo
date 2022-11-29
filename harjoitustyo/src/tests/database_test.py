import unittest
from UserRepository import user_repository
from database_connection import test_connection
from initialize_database import initialize_database_test

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        initialize_database_test()
        user_repository._connection = test_connection()
        user_repository.add_user("asd", "moi123", 1)

    def test_deleting_decreases_size(self):
        cursor = user_repository._connection.cursor()
        orgSize = user_repository.users_size()

        cursor.execute("DELETE FROM users WHERE username='asd'")

        user_repository._connection.commit()

        self.assertEqual(user_repository.users_size(), orgSize-1)


