from tkinter import ttk, constants, StringVar
from session import session
from CourseRepository import course_repository

class CoursesOperationsView:
    def __init__(self, root, handle_main_view):
        self._root = root
        self._frame = None

        self._handle_main_view = handle_main_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        update_course_id = StringVar()
        update_course_grade = StringVar()
        add_course_name = StringVar()
        add_ects = StringVar()

        def update_grade():
            course_id = update_course_id.get()
            grade = update_course_grade.get()
            user_id = session._user_id

            course_repository.update_grade(course_id, user_id, grade)

        def add_course():
            course_name = add_course_name.get()
            ects = int(add_ects.get())
            degree_id = session._degree_id
            user_id = session._user_id

            course_repository.add_course_to_curriculum(course_name, ects, degree_id, user_id)


        heading_label = ttk.Label(master=self._frame, text="Lisää kurssi tai päivitä arvosanaa")
        heading_label.grid(row=0, column=0, columnspan=3)

        # Updating course grade
        update_main_label = ttk.Label(master=self._frame, text="Päivitä arvosanaa")

        update_id_label = ttk.Label(master=self._frame, text="Kurssin id")
        update_id_entry = ttk.Entry(master=self._frame, textvariable=update_course_id)

        update_grade_label = ttk.Label(master=self._frame, text="Arvosana")
        update_grade_entry = ttk.Entry(master=self._frame, textvariable=update_course_grade)

        update_button = ttk.Button(
            master=self._frame,
            text="Päivitä arvosanaa",
            command=lambda: update_grade()
        )

        update_main_label.grid(row=1, column=0, columnspan=2)
        update_id_label.grid(row=2, column=0)
        update_id_entry.grid(row=2, column=1)
        update_grade_label.grid(row=3, column=0)
        update_grade_entry.grid(row=3, column=1)
        update_button.grid(row=4, column=0, columnspan=2)



        # Adding a new course
        add_main_label = ttk.Label(master=self._frame, text="Lisää kurssi opintosuunnitelmaan")

        add_name_label = ttk.Label(master=self._frame, text="Kurssin nimi")
        add_name_entry = ttk.Entry(master=self._frame, textvariable=add_course_name)

        add_ects_label = ttk.Label(master=self._frame, text="Opintopisteiden määrä")
        add_ects_entry = ttk.Entry(master=self._frame, textvariable=add_ects)

        add_button = ttk.Button(
            master=self._frame,
            text="Lisää kurssi",
            command=lambda: add_course()
        )

        add_main_label.grid(row=5, column=0, columnspan=2)
        add_name_label.grid(row=6, column=0)
        add_name_entry.grid(row=6, column=1)
        add_ects_label.grid(row=7, column=0)
        add_ects_entry.grid(row=7, column=1)
        add_button.grid(row=8, column=0, columnspan=2)

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_main_view
        )
        return_button.grid(row=9, column=0, columnspan=2)