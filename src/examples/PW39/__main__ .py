from tkinter import *
from src.open_tasks import open_it
import os


def first_task():
    window = Tk()
    window.geometry('500x250')

    def test():
        if v1.get() == 2:
            l1 ['text' ]= 'Молодець!'
        else:
            l1 ['text' ]= 'He вірHо !!! '
    l1 = Label(text = 'Яка найменша одиниця вимірювання інформації?', width=40,
            height=2,font=('Comic Sans', 14, 'bold'),)
    l1.pack()

    v1 = IntVar()
    r1 = Radiobutton(text=' Байт', variable=v1,value=0)
    r2 = Radiobutton(text=' Бод ', variable=v1, value=1)
    r3 = Radiobutton(text='6iT', variable=v1,value=2)
    r1.pack()
    r2.pack()
    r3.pack()

    b1 = Button(text=' Перевірити', width=10, height=3, command=test)
    b1.pack()

    window .mainloop()

def second_task():
    window = Tk()
    window.geometry('500x250')

    def test():
        if (cvar1.get() == True and cvar2.get() == False
            and cvar3.get() == False and cvar4.get() == True ):
            l1 ['text' ]= 'Молодець!'
        else:
            l1['text' ]= 'He Bipнo !!! '

    l1 = Label(text = 'В яких одиницях вимірюється потужність?',
        width=40, height=2,font=('Comic Sans', 14, 'bold'),)
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
    c4 = Checkbutton(text="Мегaвaт", variable=cvar4, onvalue=1, offvalue=0)
    c4.pack(anchor=W)

    b1 = Button(text='Перевірити', width=10, height=3, command=test)
    b1.pack()

    window .mainloop()


def third_trask():
    def addltem():
        lbox.insert(END, entry.get())
        entry.delete(0, END)

    def delList():
        select = list(lbox.curselection())
        select.reverse()
        for i in select:
            lbox.delete(i)

    def saveList():
        f= open('list01.txt', 'w')
        f.writelines("\n".join(lbox.get(0, END)))
        f.close()
    window = Tk()
    window.geometry('250x150')

    lbox = Listbox(selectmode=EXTENDED)
    lbox.pack(side=LEFT)
    scroll = Scrollbar(command=lbox.yview)
    scroll.pack(side=LEFT, fill=Y)
    lbox.config(yscrollcommand=scroll.set)

    f = Frame()
    f.pack(side=LEFT, padx=10)
    entry = Entry(f)
    entry.pack(anchor=N)
    badd = Button(f, text="Add", command=addltem)
    badd.pack(fill=X)
    bdel = Button(f, text="Delete", command=delList)
    bdel.pack(fill=X)
    bsave = Button(f, text="Save", command=saveList)
    bsave.pack(fill=X)

    window .mainloop()


try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
