import unittest
from database_connection import test_connection
from initialize_database import initialize_database_test
from services.services import sisu_service, UsernameInUseError, InvalidCredentialsError, InvalidGradeError, NegativeEctsError


class TestUserRepository(unittest.TestCase):
    
    def setUp(self):
        initialize_database_test()
        sisu_service.user_repository._connection = test_connection()
        sisu_service.course_repository._connection = test_connection()

    # _s_ means services test
    def test_s_services_update_logged_in(self):
        sisu_service.update_logged_in_ids(2, 3)

        self.assertEqual(sisu_service.user_id, 2)
        self.assertEqual(sisu_service.degree_id, 3)

    def test_s_register_valid(self):
        org_size = sisu_service.users_size()

        sisu_service.register("rase5", "moi123", 1)

        self.assertEqual(sisu_service.users_size(), org_size + 1)

    def test_s_register_not_valid(self):

        sisu_service.register("rase5", "moi123", 1)
        self.assertRaises(
            UsernameInUseError,
            lambda: sisu_service.register("rase5", "moi123", 1)
        )

    def test_s_user_id_and_degree_id(self):
        sisu_service.register("rase5", "moi123", 1)
        sisu_service.register("r", "moi13", 1)
        sisu_service.register("matikka", "moia13", 2)

        ids = sisu_service.get_user_id_and_degree_id("matikka")

        self.assertEqual(ids[0], 3)
        self.assertEqual(ids[1], 2)

    def test_s_authenticate_login_not_valid(self):
        sisu_service.register("rase5", "moi123", 1)

        self.assertRaises(
            InvalidCredentialsError,
            lambda: sisu_service.authenticate_login("rase5", "321iom")
        )

    def test_s_update_grade_low(self):
        sisu_service.register("rase5", "moi123", 1)

        self.assertRaises(
            InvalidGradeError,
            lambda: sisu_service.update_grade(1, 1, 6)
        )

    def test_s_update_grade_high(self):
        sisu_service.register("rase5", "moi123", 1)

        self.assertRaises(
            InvalidGradeError,
            lambda: sisu_service.update_grade(1, 1, -1)
        )

    def test_s_add_curriculum_negative_ects(self):
        sisu_service.register("rase5", "moi123", 1)

        self.assertRaises(
            NegativeEctsError,
            lambda: sisu_service.add_course_to_curriculum("a", -1, 1, 1)
        )

    def test_s_total_ects_in_curriculum_zero_beginning(self):
        sisu_service.register("rase5", "moi123", 1)

        # this amount needs to be changed if more mandatory courses are added
        self.assertEqual(sisu_service.total_ects_in_curriculum(1), 25)

    def test_s_total_ects_in_curriculum_zero_beginning(self):
        sisu_service.register("rase5", "moi123", 1)

        self.assertEqual(sisu_service.completed_ects(1), 0)

    def test_s_total_ects_updated(self):
        sisu_service.register("rase5", "moi123", 1)
        sisu_service.add_course_to_curriculum("Alon", 10, 1, 1)

        self.assertEqual(sisu_service.total_ects_in_curriculum(1), 35)

    def test_s_gpa_correctly_one_course(self):
        sisu_service.register("rase5", "moi123", 1)
        sisu_service.add_course_to_curriculum("Alon", 10, 1, 1)
        sisu_service.update_grade(11, 1, 5)

        self.assertEqual(sisu_service.calculate_gpa(1), 5)

    def test_s_gpa_correctly_many_courses(self):
        sisu_service.register("rase5", "moi123", 1)
        sisu_service.add_course_to_curriculum("Alon", 10, 1, 1)
        sisu_service.update_grade(1, 1, 0)
        sisu_service.update_grade(2, 1, 0)
        sisu_service.update_grade(11, 1, 5)

        self.assertEqual(sisu_service.calculate_gpa(1), 2.5)