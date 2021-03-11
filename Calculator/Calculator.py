import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image  
import os
FlexyPath = os.path.dirname(os.path.abspath(__file__))
window = tk.Tk()


def errorMessage():
    def clear():
        e1.delete(0, "end")
        errWin.destroy()

    errWin = tk.Toplevel()
    errWin.wm_title("Window")

    l = tk.Label(errWin, text="Please Enter A Valid Number")
    l.grid(row=0, column=0)

    b = tk.Button(errWin, text="Okay", command=clear)
    b.grid(row=1, column=0)


def add():
    l = e1.get()
    l = l.split( )
    try:
        l = list(map(int, l))
    except:
        errorMessage()
    e1.delete(0, "end")
    e1.insert(0, str(sum(l)))


def subtract():
    l = e1.get()
    l = l.split( )
    try:
        l = list(map(int, l))
    except:
        errorMessage()
    e1.delete(0, "end")
    e1.insert(0, str(l[0]- sum(l[1:])))
    

def multiply():
    l = e1.get()
    l = l.split( )
    try:
        l = list(map(int, l))
    except:
        errorMessage()
    ans = 1
    for i in l:
        ans = i * ans
    e1.delete(0, "end")
    e1.insert(0, ans)


def divide():
    l = e1.get()
    l = l.split( )
    try:
        l = list(map(int, l))
    except:
        errorMessage()
    ans = 1
    counter = 0
    for i in l:
        counter += 1
        if counter == 1:
            ans = i / ans
        else:
            ans = ans / i
    e1.delete(0, "end")
    e1.insert(0, ans)


window.minsize(250, 100)
window.title("Calculator")


pImg = PhotoImage(file = FlexyPath + "/+.gif")
xImg = PhotoImage(file = FlexyPath + "/mult.gif")
minImg = PhotoImage(file = FlexyPath + "/-.gif")
divideImg = PhotoImage(file = FlexyPath + "/divide.gif")


dividePhotoImage = divideImg.subsample(3, 3) 
timesPhotoImage = xImg.subsample(3, 3) 
addPhotoImage = pImg.subsample(3, 3) 
minPhotoImage = minImg.subsample(3, 3) 

tk.Label(window, text="Numbers:").grid(row=0)

divB = tk.Button(window, image = dividePhotoImage, text ="/", command = divide)
addB = tk.Button(window, image = addPhotoImage, text ="+", command = add)
subB = tk.Button(window, image = minPhotoImage, text ="-", command = subtract)
mulB = tk.Button(window, image = timesPhotoImage, text ="x", command = multiply)

e1 = tk.Entry(window)

divB.place(x=190, y=40)
mulB.place(x=130, y=40)
subB.place(x=70, y=40)
addB.place(x=10, y=40)
e1.grid(row=0, column=1)


window.mainloop()