from tkinter import ttk, constants, IntVar, StringVar
from session import session
from CourseRepository import course_repository

class MainView:
    def __init__(self, root, handle_login):
        self._root = root
        self._frame = None

        self._handle_login = handle_login

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

        heading_label.grid(row=0, column=0, columnspan=2)

        i = 0
        courses = course_repository.get_course_data_mainpage()
        length = len(courses)

        for course in courses:
            output = str(course[0]) + ", "
            if course[1] == -1:
                output = output + "ei suoritettu"
            else:
                output + course[1]

            label = ttk.Label(master=self._frame, text=output)
            label.grid(row=i+1, column=0)
            i += 1


        logout_button.grid(row=length+2, column=0, columnspan=2)