from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
root.geometry('600x600')

stan = Frame(root, bg="grey", bd=5, relief=SUNKEN)
stan.grid(padx=10, pady=10, sticky="nw")

frame_name = Label(stan, text="Оберіть стан машини:", bg="grey", fg="white")
frame_name.pack(side="top")

radio_btn = IntVar()

new = Radiobutton(stan, text="Нове", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=1)
new.pack()
by = Radiobutton(stan, text="Вживане", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=2)
by.pack(padx=10, pady=10)

rokiv = Frame(root, bg="grey", bd=5, relief=SUNKEN)
rokiv.grid(padx=10, pady=10, sticky="nw")

frame2_name = Label(rokiv, text="Оберіть вік машини:", bg="grey", fg="white")
frame2_name.pack(side="top")

nove = Radiobutton(rokiv, text="Нове", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=3)
do5 = Radiobutton(rokiv, text="До 5 років", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=4)
vid5 = Radiobutton(rokiv, text="Від 5 до 10 років", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=5)
bilshe10 = Radiobutton(rokiv, text="Більше 10", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=6)

nove.pack()
do5.pack(padx=10, pady=10)
vid5.pack(padx=10, pady=10)
bilshe10.pack(padx=0, pady=10)

mark = Frame(root, bg="grey", bd=5, relief=SUNKEN)
mark.grid(padx=10, pady=10, sticky="nw")

frame3_name = Label(mark, text="Марка машини:", bg="grey", fg="white")
frame3_name.pack(side="top")
audi = Radiobutton(mark, text="Audi", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=7)
ford = Radiobutton(mark, text="Ford", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=8)
bmw = Radiobutton(mark, text="BMW", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=9)
mercedes = Radiobutton(mark, text="Mercedes", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=10)
wolkcvagen = Radiobutton(mark, text="Wlkcvagen", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=11)
insha = Radiobutton(mark, text="Інша", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=12)

audi.pack()
ford.pack(padx=0, pady=10)
bmw.pack(padx=0, pady=10)
mercedes.pack(padx=0, pady=10)
wolkcvagen.pack(padx=0, pady=10)
insha.pack(padx=0, pady=10)

duzel = Frame(root, bg="grey", bd=5, relief=SUNKEN)
duzel.grid(row=0, column=2, padx=10, pady=10, sticky="n")

frame5_name = Label(duzel, text="Топливо:", bg="grey", fg="white")
frame5_name.pack(side="top")

benz = Radiobutton(duzel, text="Бензин", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=13)
duz = Radiobutton(duzel, text="Дизель", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=14)

benz.pack()
duz.pack(padx=0, pady=10)

dvugyn = Frame(root, bg="grey", bd=5, relief=SUNKEN)
dvugyn.grid(row=1, column=2, padx=10, pady=10, sticky="nw", rowspan=2)

frame4_name = Label(dvugyn, text="Об'єм двигуна:", bg="grey", fg="white")
frame4_name.pack(side="top")
men1200 = Radiobutton(dvugyn, text="Меньше 1200л", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=15)
do1500 = Radiobutton(dvugyn, text="1200 - 1500л", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=16)
do2200 = Radiobutton(dvugyn, text="1500 - 2200л", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=17)
bilsh2200 = Radiobutton(dvugyn, text="Більше 2200л", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=18)

men1200.pack()
do1500.pack(padx=0, pady=10)
do2200.pack(padx=0, pady=10)
bilsh2200.pack(padx=0, pady=10)

vurobnyk = Frame(root, bg="grey", bd=5, relief=SUNKEN)
vurobnyk.grid(row=1, column=3, padx=10, pady=10, sticky="nw")

frame4_name = Label(vurobnyk, text="Країна - виробник:", bg="grey", fg="white")
frame4_name.pack(side="top")
azia = Radiobutton(vurobnyk, text="Азія", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=19)
america = Radiobutton(vurobnyk, text="Америка", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=20)
sheurop = Radiobutton(vurobnyk, text="Східна Європа", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=21)
zaheurop = Radiobutton(vurobnyk, text="Західна Європа", bg="grey", fg="white", width=10, padx=5, relief=SUNKEN, variable=radio_btn, value=22)

azia.pack()
america.pack(padx=0, pady=10)
sheurop.pack(padx=0, pady=10)
zaheurop.pack(padx=0, pady=10)
def selectedcol():
    selected_color = kolor.get()
    colorkvadrat.config(bg=selected_color)


kolor = Combobox(root, foreground="grey")
kolor['values'] = ("Red", "Blue", "Black", "White", "Purple", "Green")
kolor.current(4)
kolor.grid(row=0, column=3, padx=10, pady=10, sticky="n")

select = Button(root, text="Показати вибраний колір", command=selectedcol, bg="grey", fg="white", relief=SUNKEN)
select.grid(row=0, column=3, padx=1, pady=1)

selectedclrlabel = Label(root, text="", bg="grey", fg="white")
selectedclrlabel.grid(row=0, column=3, padx=10, pady=10)

colorkvadrat = Label(root, width=5, height=2, bg="white", borderwidth=1, relief="solid")
colorkvadrat.grid(row=0, column=3)


def mark_choice():
    mark_choices = {
        7: "Audi",
        8: "Ford",
        9: "BMW",
        10: "Mercedes",
        11: "Wlkcvagen",
        12: "Інша"
    }
    return mark_karoche.get(karoche_mark.get(), "Немає вибору")


def duzel_choice():
    duzel_choices = {
        13: "Бензин",
        14: "Дизель"
    }
    return duzel_choices.get(karoche_duzel.get(), "Немає вибору")


def dvugyn_choice():
    dvugyn_karoche = {
        15: "Меньше 1200л",
        16: "1200 - 1500л",
        17: "1500 - 2200л",
        18: "Більше 2200л"
    }
    return dvugyn_karoche.get(radio_i_dvugyn.get(), "Немає вибору")


def vurobnyk_choice():
    vurobnyk_karoche = {
        19: "Азія",
        20: "Америка",
        21: "Східна Європа",
        22: "Західна Європа"
    }
    return vurobnyk_karoche.get(radio_i_vurobnyk.get(), "Немає вибору")


def resultatu(entry):
    state = {1: "Нове", 2: "Вживане"}[radio_karoche.get()]
    age = {1: "Нове", 2: "До 5 років", 3: "Від 5 до 10 років", 4: "Більше 10"}[radio_i_age.get()]
    select_color = kolor.get()
    mark_karoche = mark_choice()
    duzel_karoche = duzel_choice()
    dvugyn_karoche = dvugyn_choice()
    vurobnyk_karoche = vurobnyk_choice()

    result_text = f"Стан машини: {state}, Вік машини: {age}, Колір: {select_color}, Марка машини: {mark_karoche}, Топливо: {duzel_karoche}, Об'єм двигуна: {dvugyn_karoche}, Країна - виробник: {vurobnyk_karoche}"
    entry.insert(0, result_text)

fffff = Frame(root, bg="grey", bd=5, relief=SUNKEN)
fffff.grid(row=2, column=2, padx=10, pady=10, sticky="nw")

fname = Label(fffff, text="Результати вибору:", bg="grey", fg="white")
fname.pack(side="top")

fbutton = Button(fffff, text="Результати вибору:", command=lambda: resultatu(entry), bg="grey", fg="white")
fbutton.pack()

entry = Entry(fffff, bg="grey", relief=SUNKEN, width=50, selectforeground="white")
entry.pack()
resultatu(entry)
def new_oputyvannya():
    text = ""
    entry.delete(0, END)
    entry.insert(0, text)

nove_oput = Button(root, text="Нове опитування", command=new_oputyvannya, bg="grey", fg="white", relief=SUNKEN)
nove_oput.grid()

root.mainloop()