from tkinter import *
import os
from src.open_tasks import open_it


def fist_task():
    window = Tk()
    window.title("Program Name")
    window.geometry("600x500")
    img = PhotoImage(file="img.png")
    Label(image=img).pack()
    Label(text="Unknown", font=("Times new  roman", 25, "bold ")).pack()
    Label(
        text="Group",
        font=("Arial", 25, "bold underline"),
        relief="ridge",
        borderwidth="10",
        fg="white",
        bg="purple",
    ).pack()
    window.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
