from tkinter import ttk, constants, StringVar
from services.services import sisu_service, InvalidGradeError, NegativeEctsError

class CoursesOperationsView:
    def __init__(self, root, handle_main_view):
        self._root = root
        self._frame = None

        self._error_variable = None
        self._error_label = None

        self._handle_main_view = handle_main_view

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=12, column=0, columnspan=2)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        update_course_id = StringVar()
        update_course_grade = StringVar()
        add_course_name = StringVar()
        add_ects = StringVar()
        delete_id = StringVar()
        self._error_variable = StringVar(self._frame)

        def update_grade():
            course_id = update_course_id.get()
            grade = update_course_grade.get()
            user_id = sisu_service.user_id

            if len(course_id) <= 0:
                self._handle_error("Syötä kurssin id")
                return
            if len(grade) <= 0:
                self._handle_error("Syötä arvosana")
                return

            if not course_id.isnumeric():
                self._handle_error("Syötä kelpo kurssin id")
                return
            if not grade.isnumeric():
                self._handle_error("Syötä kelpo arvosana")
                return


            try:
                sisu_service.update_grade(course_id, user_id, grade)
            except InvalidGradeError:
                self._handle_error("Arvosanan pitää olla väliltä 0-5")
                return

            self._error_variable.set("")


        def add_course():
            course_name = add_course_name.get()
            ects = add_ects.get()
            degree_id = sisu_service.degree_id
            user_id = sisu_service.user_id

            if len(course_name) <= 0:
                self._handle_error("Syötä kurssin nimi")
                return
            if len(ects) <= 0:
                self._handle_error("Syötä opintopisteiden määrä")
                return

            if not ects.isnumeric():
                self._handle_error("Syötä kelpo opintopisteiden määrä")
                return

            try:
                sisu_service.add_course_to_curriculum(course_name, ects, degree_id, user_id)
            except NegativeEctsError:
                self._handle_error("Opintopisteet eivät voi olla negatiivisia")
                return

            self._error_variable.set("")

        def delete_enrollment():
            del_id = delete_id.get()
            user_id = sisu_service.user_id

            sisu_service.delete_enrollment(user_id, del_id)


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

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
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


        # Deleting a enrollment
        delete_main_label = ttk.Label(master=self._frame, text="Poista kurssi opintosuunnitelmasta")

        delete_id_label = ttk.Label(master=self._frame, text="Kurssin id")
        delete_id_entry = ttk.Entry(master=self._frame, textvariable=delete_id)

        delete_button = ttk.Button(
            master=self._frame,
            text="Poista kurssi",
            command=lambda: delete_enrollment()
        )

        delete_main_label.grid(row=9, column=0, columnspan=2)
        delete_id_label.grid(row=10, column=0)
        delete_id_entry.grid(row=10, column=1)
        delete_button.grid(row=11, column=0, columnspan=2)

        return_button = ttk.Button(
            master=self._frame,
            text="Takaisin",
            command=self._handle_main_view
        )
        return_button.grid(row=13, column=0, columnspan=2)