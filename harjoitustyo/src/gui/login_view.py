from tkinter import ttk, constants, StringVar
from services.services import sisu_service, InvalidCredentialsError


class LoginView:
    def __init__(self, root, handle_register, handle_main):
        self._root = root
        self._frame = None

        self._username = None
        self._password = None

        self._error_variable = None
        self._error_label = None

        self._handle_register = handle_register
        self._handle_main = handle_main

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _handle_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=5, column=0, columnspan=2)

    def  _login_handler(self):
        
        username = self._username.get()
        password = self._password.get()

        try:
            sisu_service.authenticate_login(username, password)
        except InvalidCredentialsError:
            self._handle_error("Väärä käyttäjätunnus tai salasana")
            return

        ids = sisu_service.get_user_id_and_degree_id(username)
        sisu_service.update_logged_in_ids(ids[0], ids[1])

        self._handle_main()
            
    
    def _initialize(self):
        
        self._frame = ttk.Frame(master=self._root)

        sisu_service.update_logged_in_ids(0, 0)

        self._username = StringVar()
        self._username.set("")
        self._password = StringVar()
        self._password.set("")
        self._error_variable = StringVar(self._frame)
        
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

        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        login_button.grid(row=4, column=0, columnspan=2)
        register_button.grid(row=7, column=0, columnspan=2)
