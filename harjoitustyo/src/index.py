from tkinter import Tk
from gui.ui import UI


def main():
    window = Tk()
    window.title("Sisu 2.0")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
