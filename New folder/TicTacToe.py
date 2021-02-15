# import tkinter as tk
# window = tk.Tk()
# window.minsize(250, 100)
# window.title("TicTacToe")
# counter = "x"
# def Change():
#     global counter
#     print("hello")
#     if counter == "x":
#         print(LT)
#         LT_text.set("b")
#         counter = "o"


#     else:
#         counter = "x"

#     return counter
#     # LT = tk.Button(window, text =counter, command = Change)

# LT_text = tk.StringVar()


# LT = tk.Button(window, text =LT_text, command = Change)
# LT.pack()
# LT.grid(row=0, column=1)
# window.mainloop()

import tkinter as tk

root = tk.Tk()
root.minsize(250, 100)
root.title("TicTacToe")
counter = "x"

def update_btn_text():
    global counter
    print("hello")
    if counter == "x":
        print(LT)
        LT_text.set(counter)
        counter = "o"
    else:
        LT_text.set(counter)
        counter = "x"


LT_text = tk.StringVar()
LT = tk.Button(root, textvariable=LT_text, command=update_btn_text)

LT.pack()

root.mainloop()