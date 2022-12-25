from tkinter import ttk, constants
from services.services import sisu_service

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

        user_id = sisu_service.user_id

        gpa_str = sisu_service.calculate_gpa(user_id)
        gpa_text = "Opintojen keskiarvo: " + str(gpa_str)[0:4]
        gpa_label = ttk.Label(master=self._frame, text=gpa_text)
        gpa_label.grid(row=2, column=0)

        total_ects = sisu_service.total_ects_in_curriculum(user_id)
        current_ects = sisu_service.completed_ects(user_id)
        percent = int(current_ects / total_ects * 100)
        ects_text = str(current_ects) + " / " + str(total_ects) + " op (" + str(percent) + "% suoritettu)"


        ects_label = ttk.Label(master=self._frame, text=ects_text)
        ects_label.grid(row=3, column=0)

        i = 0
        courses = sisu_service.get_course_data_mainpage(user_id)
        length = len(courses)

        for course in courses:
            output = str(course[0]) + " (id: " + str(course[2]) + "), arvosana: "
            if course[1] == -1:
                output += "ei suoritettu"
            else:
                output += str(course[1])

            label = ttk.Label(master=self._frame, text=output)

            label.grid(row=i+4, column=0)
            i += 1


        logout_button.grid(row=length+4, column=0, columnspan=2)