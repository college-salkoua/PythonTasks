
import tkinter as tk

# Створення вікна
root = tk.Tk()
root.geometry('250x250')

# Створення полотна
canvas = tk.Canvas(root, width=1000, height=1000)
canvas.pack()

canvas.create_rectangle(50,110, 70, 160, outline='purple')
# Запуск головного циклу
root.mainloop()

