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

        def update_grade(self):
            course_id = update_course_id.get()
            grade = update_course_grade.get()
            user_id = session._user_id

            course_repository.update_grade(course_id, user_id, grade)

        heading_label = ttk.Label(master=self._frame, text="Lisää kurssi tai päivitä arvosanaa")
        heading_label.grid(row=0, column=0, columnspan=3)

        update_main_label = ttk.Label(master=self._frame, text="Päivitä arvosanaa")
        update_id_label = ttk.Label(master=self._frame, text="Kurssin id")
        update_id_entry = ttk.Entry(master=self._frame, textvariable=update_course_id)
        update_grade_label = ttk.Label(master=self._frame, text="Arvosana")
        update_grade_entry = ttk.Entry(master=self._frame, textvariable=update_course_grade)
        update_button = ttk.Button(
            master=self._frame,
            text="Päivitä arvosanaa",
            command=lambda: update_grade(self)
        )

        update_main_label.grid(row=1, column=0, columnspan=2)
        update_id_label.grid(row=2, column=0)
        update_id_entry.grid(row=2, column=1)
        update_grade_label.grid(row=3, column=0)
        update_grade_entry.grid(row=3, column=1)
        update_button.grid(row=4, column=0, columnspan=2)

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_main_view
        )
        return_button.grid(row=100, column=0, columnspan=2)