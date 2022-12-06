from tkinter import ttk, constants, StringVar
from UserRepository import user_repository
from CourseRepository import course_repository
from session import session


class LoginView:
    def __init__(self, root, handle_register, handle_main):
        self._root = root
        self._frame = None

        self._username = None
        self._password = None

        self._handle_register = handle_register
        self._handle_main = handle_main

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def  _login_handler(self):
        
        username = self._username.get()
        password = self._password.get()

        if user_repository.authenticate_login(username, password):

            # update session
            ids = course_repository.get_user_id_and_degree_id(username)
            session.set_vars(ids[0], ids[1])

            self._handle_main()
    
    def _initialize(self):
        
        self._frame = ttk.Frame(master=self._root)

        session.set_vars(0, 0)

        self._username = StringVar()
        self._username.set("")
        self._password = StringVar()
        self._password.set("")
        
        heading_label = ttk.Label(master=self._frame, text="Kirjaudu sisään")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        username_entry = ttk.Entry(master=self._frame, textvariable=self._username)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        password_entry = ttk.Entry(master=self._frame, textvariable=self._password)

        login_button = ttk.Button(
            master=self._frame, 
            text="Kirjaudu sisään", 
            command=self._login_handler
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Tai luo tunnus",
            command=self._handle_register
        )

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        login_button.grid(row=4, column=0, columnspan=2)
        register_button.grid(row=6, column=0, columnspan=2)
