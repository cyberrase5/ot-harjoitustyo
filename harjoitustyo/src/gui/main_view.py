from tkinter import ttk, constants, IntVar, StringVar
from session import session
from CourseRepository import course_repository

class MainView:
    def __init__(self, root, handle_login, handle_course_operations):
        self._root = root
        self._frame = None

        self._handle_login = handle_login
        self._handle_course_operations = handle_course_operations

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Kurssit")

        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._handle_login
        )

        course_operations_button = ttk.Button(
            master=self._frame,
            text="Hallitse kursseja",
            command=self._handle_course_operations
        )

        heading_label.grid(row=0, column=0, columnspan=2)
        course_operations_button.grid(row=1, column=0)

        i = 0
        courses = course_repository.get_course_data_mainpage()
        length = len(courses)

        for course in courses:
            output = str(course[0]) + " (id: " + str(course[2]) + "), arvosana: "
            if course[1] == -1:
                output += "ei suoritettu"
            else:
                output += str(course[1])

            label = ttk.Label(master=self._frame, text=output)

            label.grid(row=i+2, column=0)
            i += 1


        logout_button.grid(row=length+2, column=0, columnspan=2)