from tkinter import Tk, ttk, IntVar, StringVar
from UserRepository import user_repository

class UI:
    def __init__(self, root):
        self._root = root
        self._username = None
        self._password = None
        self._degree_id = None

    def start(self):

        def create_user(self):
            u = username.get()
            p = password.get()
            user_repository.add_user(u, p, 1)

        username = StringVar()
        username.set("")
        password = StringVar()
        password.set("")
        
        heading_label = ttk.Label(master=self._root, text="Rekisteröidy")

        username_label = ttk.Label(master=self._root, text="Käyttäjätunnus")
        username_entry = ttk.Entry(master=self._root, textvariable=username)

        password_label = ttk.Label(master=self._root, text="Salasana")
        password_entry = ttk.Entry(master=self._root, textvariable=password)

        radiobutton1 = ttk.Radiobutton(master=self._root, text="Tietojenkäsittelytieteen kandiohjelma", variable=self._degree_id, var=1)

        radiobutton2 = ttk.Radiobutton(master=self._root, text="Älä paina", variable=self._degree_id, var=2)

        button = ttk.Button(master=self._root, text="Luo käyttäjä", command=lambda: create_user(self))

        heading_label.grid(row=0, column=0, columnspan=2)

        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)

        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)

        radiobutton1.grid(row=3, column=0)

        radiobutton2.grid(row=3, column=1)

        button.grid(row=4, column=0, columnspan=2)

