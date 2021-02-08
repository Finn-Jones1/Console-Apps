import tkinter as tk
window = tk.Tk()

def calc():
    l = e1.get()
    l = l.split( )
    l = list(map(int, l))

    print(l)
    print(str(sum(l)))

tk.Label(window, text="Numbers:").grid(row=0)
e1 = tk.Entry(window)
B = tk.Button(window, text ="Hello", command = calc)

e1.grid(row=0, column=1)



calc()
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