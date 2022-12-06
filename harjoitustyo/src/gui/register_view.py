from tkinter import ttk, constants, IntVar, StringVar
from UserRepository import user_repository


class RegisterView:
    def __init__(self, root, handle_login):
        self._root = root
        self._frame = None

        self._username = None
        self._password = None
        self._degree_id = None

        self._handle_login = handle_login

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        def create_user(self):
            u = username.get()
            p = password.get()
            di = degree_id.get()
            user_repository.add_user(u, p, di)

        username = StringVar()
        username.set("")
        password = StringVar()
        password.set("")
        degree_id = IntVar()
        
        heading_label = ttk.Label(master=self._frame, text="Rekisteröidy")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        username_entry = ttk.Entry(master=self._frame, textvariable=username)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        password_entry = ttk.Entry(master=self._frame, textvariable=password)

        radiobutton1 = ttk.Radiobutton(master=self._frame, text="Tietojenkäsittelytieteen kandiohjelma", variable=degree_id, value=1)
        radiobutton2 = ttk.Radiobutton(master=self._frame, text="Älä paina", variable=degree_id, value=2)

        button = ttk.Button(master=self._frame, text="Luo käyttäjä", command=lambda: create_user(self))

        login_button = ttk.Button(
            master=self._frame,
            text="Tai kirjaudu sisään",
            command=self._handle_login
        )

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        radiobutton1.grid(row=3, column=0)

        radiobutton2.grid(row=3, column=1)

        button.grid(row=4, column=0, columnspan=2)
        login_button.grid(row=6, column=0, columnspan=2)