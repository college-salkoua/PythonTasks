from tkinter import *
from tkinter import filedialog, messagebox
import tkinter
from tkinter.colorchooser import askcolor
from src.open_tasks import open_it
import os


def first_task():
    def open_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                text.delete('1.0', tkinter.END)
                text.insert(tkinter.END, file.read())

    def save_file():
        file_path = filedialog.askopenfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get('1.0', tkinter.END))

    def color_bg():
        (triple, hex_color) = askcolor()
        if hex_color:
            text.config(bg=hex_color)

    def color_fg():
        (triple, hex_color) = askcolor()
        if hex_color:
            text.config(fg=hex_color)

    def about_bt():
        text.showinfo('Автор: Чуйко Микола, це програма Текстовий редактор')

    root = Tk()
    root.title("Текстовий редактор")

    menu = Menu(root)
    root.config(menu=menu)

    file_menu = Menu(root, tearoff=0)
    menu.add_cascade(label="Файл", menu=file_menu)
    file_menu.add_command(label="Відкрити", command=open_file)
    file_menu.add_command(label="Зберегти", command=save_file)
    file_menu.add_separator()
    file_menu.add_command(label="Вихід", command=root.quit)
    color_menu = Menu(root, tearoff=0)
    menu.add_cascade(label="Колір", menu=color_menu)
    color_menu.add_command(label="Колір фону", command=color_bg)
    color_menu.add_command(label="Колір шрифту", command=color_fg)
    about_menu = Menu(root, tearoff=0)
    menu.add_cascade(label="Про автора",menu=about_menu)
    about_menu.add_command(label="Про автора", command=about_bt)
    text = Text(root, wrap="word")
    text.pack(expand=True, fill="both")

    root.mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
