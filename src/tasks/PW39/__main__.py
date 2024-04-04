from tkinter import *
from src.open_tasks import open_it
import os


def first_task():
    def show_phone_number():
        friend_name = selected_friend.get()
        phone_numbers = {
            "Чуйко Микола": "+38077777777777",
            "Грабовський Віталій": "+38088888888888",
            "Прокопчук Олександр": "+38099999999999"
        }
        phone_number = phone_numbers.get(friend_name, "Номер телефону не знайдено")
        phone_number_label.config(text=phone_number)
    root=Tk()
    root.title("Номер телефону друзів")
    selected_friend=StringVar()
    friends=["Чуйко Микола", "Грабовський Віталій", "Прокопчук Олександр"]
    for friend in friends:
        Radiobutton(root, text=friend, variable=selected_friend, value=friend, indicatoron=0, command=show_phone_number).pack(anchor=W, side=RIGHT)
    phone_number_label=Label(root, text="", pady=100)
    phone_number_label.pack()
    root.geometry("600x100")
    root.mainloop()


def second_task():
    window = Tk()
    window.geometry('500x1024')

    def test1():
        if (cvar1.get() == True and cvar2.get() == False and cvar3.get() == False and cvar4.get() == True ):
            l1['text' ]= 'Молодець!'
        else:
            l1['text']= 'Не вірно!! '

    def test2():
        if (cvar1.get() == False and cvar2.get() == True and cvar3.get() == True and cvar4.get() == True ):
            l2['text' ]= 'Молодець!'
        else:
            l2['text']= 'Не вірно!! '


    def test3():
        if v1.get() == 1:
            l3['text' ]= 'Молодець!'
        else:
            l3['text' ]= 'Не вірно!!! '

    def test4():
        if v2.get() == 1:
            l4['text' ]= 'Молодець!'
        else:
            l4['text' ]= 'Не вірно!!! '       
            

    l1 = Label(text = 'В яких одиницях вимірюється потужність?', width=40, height=2,font=('Comic Sans', 14, 'bold'),)
    l1.pack()

    cvar1 = BooleanVar()
    cvar1.set(0)
    c1 = Checkbutton(text="BaT", variable=cvar1, onvalue=1, offvalue=0)
    c1.pack(anchor=W)
    cvar2 = BooleanVar()
    cvar2.set(0)
    c2 = Checkbutton(text="Джоуль", variable=cvar2, onvalue=1, offvalue=0)
    c2.pack(anchor=W)
    cvar3 = BooleanVar()
    cvar3.set(0)
    c3 = Checkbutton(text="Вольт", variable=cvar3, onvalue=1, offvalue=0)
    c3.pack(anchor=W)
    cvar4 = BooleanVar()
    cvar4.set(0)
    c4 = Checkbutton(text="Мегават", variable=cvar4, onvalue=1, offvalue=0)
    c4.pack(anchor=W)

    b1 = Button(text='Перевірити', width=10, height=3, command=test1)
    b1.pack()


    l2 = Label(text = 'Які кольори показує світлофор?', width=40, height=2,font=('Comic Sans', 14, 'bold'),)
    l2.pack()

    cvar1 = BooleanVar()
    cvar1.set(0)
    c1 = Checkbutton(text="Рожевий", variable=cvar1, onvalue=1, offvalue=0)
    c1.pack(anchor=W)
    cvar2 = BooleanVar()
    cvar2.set(0)
    c2 = Checkbutton(text="Зелений", variable=cvar2, onvalue=1, offvalue=0)
    c2.pack(anchor=W)
    cvar3 = BooleanVar()
    cvar3.set(0)
    c3 = Checkbutton(text="Червоний", variable=cvar3, onvalue=1, offvalue=0)
    c3.pack(anchor=W)
    cvar4 = BooleanVar()
    cvar4.set(0)
    c4 = Checkbutton(text="Жовтий", variable=cvar4, onvalue=1, offvalue=0)
    c4.pack(anchor=W)

    b1 = Button(text='Перевірити', width=10, height=3, command=test2)
    b1.pack()

            
    l3 = Label(text ='Яка найблища зірка до Землі?', width=40, height=2,font=('Comic Sans', 14, 'bold'),)
    l3.pack()

    v1 = IntVar()
    r1 = Radiobutton(text='Бетельгейзе', variable=v1,value=0)
    r2 = Radiobutton(text='Сонце', variable=v1, value=1)
    r3 = Radiobutton(text='Сіріус', variable=v1,value=2)
    r1.pack()
    r2.pack()
    r3.pack()

    b1 = Button(text=' Перевірити', width=10, height=3, command=test3)
    b1.pack()

    l4 = Label(text ='Який океан найбільший?', width=40, height=2,font=('Comic Sans', 14, 'bold'),)
    l4.pack()

    v2 = IntVar()
    r4 = Radiobutton(text='Середземний', variable=v2,value=0)
    r5 = Radiobutton(text='Тихий', variable=v2, value=1)
    r6 = Radiobutton(text='Індійський', variable=v2,value=2)
    r4.pack()
    r5.pack()
    r6.pack()

    b1 = Button(text=' Перевірити', width=10, height=3, command=test4)
    b1.pack()

    window.mainloop()


def third_task():
    def move_items(source, destination):
        selected_indices = source.curselection()
        for idx in selected_indices[::-1]:
            item = source.get(idx)
            destination.insert("end", item)
            source.delete(idx)

    def move_to_shopping_list():
        move_items(products_listbox, shopping_listbox)

    def move_to_products_list():
        move_items(shopping_listbox, products_listbox)

    root=Tk()
    root.title("Список продуктів")
    products_frame=Frame(root)
    products_frame.pack(side=LEFT, padx=10, pady=10)
    products_listbox=Listbox(products_frame, selectmode=MULTIPLE)
    products_listbox.pack()
    products=["Яблука", "Банани", "Мандарини", "Молоко", "Хліб", "Яйця"]
    for product in products:
        products_listbox.insert("end", product)
    buttons_frame=Frame(root)
    buttons_frame.pack(side=LEFT, padx=10)
    to_shopping_button=Button(buttons_frame, text=">>>>", command=move_to_shopping_list)
    to_shopping_button.pack(fill=X)
    to_products_button=Button(buttons_frame, text="<<<<", command=move_to_products_list)
    to_products_button.pack(fill=X)
    shopping_frame=Frame(root)
    shopping_frame.pack(side=LEFT, padx=10, pady=10)
    shopping_listbox=Listbox(shopping_frame, selectmode=MULTIPLE)
    shopping_listbox.pack()
    root.mainloop()

try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
