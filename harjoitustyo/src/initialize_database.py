from database_connection import get_database_connection, test_connection
from repositories.CourseRepository import course_repository


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
    '''
    Creates all the mandatory courses to table courses,
    calls degree-specific "child" functions, so CS and math has its own
    '''

    insert_mandatory_courses_compsci(connection)
    insert_mandatory_courses_math(connection)


def insert_mandatory_courses_compsci(connection):

    '''
    Creates mandatory computer science degree courses, id: 1
    '''

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

def insert_mandatory_courses_math(connection):

    '''
    Creates mandatory math degree courses, id: 2
    '''

    # basic studies
    course_repository.add_course("Johdatus yliopistomatematiikkaan", 5, 2, True)
    course_repository.add_course("Lineaarialgebra ja matriisilaskenta I", 5, 2, True)
    course_repository.add_course("Raja-arvot", 5, 2, True)
    course_repository.add_course("Differentiaalilaskenta", 5, 2, True)
    course_repository.add_course("Integraalilaskenta", 5, 2, True)

    connection.commit()

def initialize_database():
    '''
    "normal" database initalization, drop old tables, create new,
    add mandatory courses
    '''
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
    insert_mandatory_courses_parent(connection)


def initialize_database_test():
    '''
    Set up test database
    '''
    connection = test_connection()
    course_repository._connection = test_connection()

    t_emtpy_tables(connection)
    insert_mandatory_courses_parent(connection)

def t_emtpy_tables(connection):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM courses")
    cursor.execute("DELETE FROM participants")

    connection.commit()

if __name__ == "__main__":
    initialize_database()
    initialize_database_test()
