from database_connection import get_database_connection, test_connection
from CourseRepository import course_repository


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')
    cursor.execute('''
        drop table if exists courses;
    ''')
    cursor.execute('''
        drop table if exists participants;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE users \
            (id SERIAL PRIMARY KEY, username TEXT UNIQUE, password TEXT, degree_id INTEGER)")
    cursor.execute(
        "CREATE TABLE courses \
            (id SERIAL PRIMARY KEY, course_name TEXT, ects INTEGER, degree_id INTEGER, mandatory BOOLEAN)")
    cursor.execute(
        "CREATE TABLE participants \
            (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users ON DELETE CASCADE, "\
                "course_id INTEGER REFERENCES courses ON DELETE CASCADE, grade INTEGER)")

    connection.commit()


def insert_mandatory_courses_parent(connection):

    insert_mandatory_courses_compsci(connection)


def insert_mandatory_courses_compsci(connection):

    # basic studies
    course_repository.add_course("Ohjelmoinnin perusteet", 5, 1, True)
    course_repository.add_course("Ohjelmoinnin jatkokurssi", 5, 1, True)
    course_repository.add_course("Johdatus tietojenkäsittelytieteeseen", 5, 1, True)
    course_repository.add_course("Tietokantojen perusteet", 5, 1, True)
    course_repository.add_course("Tietokoneen toiminta", 5, 1, True)


    # pakolliset aineopinnot

    # kieliopinnot

    # lapio yms.

    # kandi


    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_mandatory_courses_parent(connection)


def initialize_database_test():
    connection = test_connection()
    course_repository._connection = test_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_mandatory_courses_parent(connection)


if __name__ == "__main__":
    initialize_database()
    initialize_database_test()
