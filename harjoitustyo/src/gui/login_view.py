from tkinter import ttk, constants, StringVar
from UserRepository import user_repository


class LoginView:
    def __init__(self, root, handle_register):
        self._root = root
        self._frame = None

        self._root = root
        self._username = None
        self._password = None

        self._handle_register = handle_register

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        def login(self):
            u = username.get()
            p = password.get()


        username = StringVar()
        username.set("")
        password = StringVar()
        password.set("")
        
        heading_label = ttk.Label(master=self._root, text="Kirjaudu sisään")

        username_label = ttk.Label(master=self._root, text="Käyttäjätunnus")
        username_entry = ttk.Entry(master=self._root, textvariable=username)

        password_label = ttk.Label(master=self._root, text="Salasana")
        password_entry = ttk.Entry(master=self._root, textvariable=password)

        button = ttk.Button(master=self._root, text="Kirjaudu sisään", command=lambda: login(self))

        register_button = ttk.Button(
            master=self._root,
            text="Tai luo tunnus",
            command=self._handle_register
        )

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        button.grid(row=4, column=0, columnspan=2)
        register_button.grid(row=5, column=0)
