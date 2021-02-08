import tkinter as tk
window = tk.Tk()

tk.Label(window, text="Numbers:").grid(row=0)
e1 = tk.Entry(window)
e1.grid(row=0, column=1)

p = input("Type Here: ")

def hello():
    l = e1.get()
    l = l.split( )
    l = list(map(int, l)) 

    print(l)
    total = 0
    sto = 0
    counter = 0


    print(l)
    print(str(sum(l)))

hello()
window.mainloop()





def add(ls):
    total = 0
    for i in ls:
        total = int(total) + int(i)
    return total

def subtract(ls):
    total = 0
    for i in ls:
        total = int(total) - int(i)
    return total