


import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.minsize(250, 100)
root.title("TicTacToe")
counter = "x"
locaterDic = {"LT":[],"MT":[],"RT":[],"LM":[],"MM":[],"RM":[],"LB":[],"MB":[],"RB":[]}



def Change(b):
    global counter
    
    print("hello")
    
    if counter == "x":
        if b == "LT":
            LT_text.set(counter)
            locaterDic["LT"].append(counter)
        elif b == "MT":
            MT_text.set(counter)
            locaterDic["MT"].append(counter)
        elif b == "RT":
            RT_text.set(counter)
            locaterDic["RT"].append(counter)
        elif b == "LM":
            LM_text.set(counter)
            locaterDic["LM"].append(counter)
        elif b == "MM":
            MM_text.set(counter)
            locaterDic["MM"].append(counter)
        elif b == "RM":
            RM_text.set(counter)
            locaterDic["RM"].append(counter)
        elif b == "LB":
            LB_text.set(counter)
            locaterDic["LB"].append(counter)
        elif b == "MB":
            MB_text.set(counter)
            locaterDic["MB"].append(counter)
        elif b == "RB":
            RB_text.set(counter)
            locaterDic["RB"].append(counter)  

        counter = "o"
    else:
        if b == "LT":
            LT_text.set(counter)
            locaterDic["LT"].append(counter)
        elif b == "MT":
            MT_text.set(counter)
            locaterDic["MT"].append(counter)
        elif b == "RT":
            RT_text.set(counter)
            locaterDic["RT"].append(counter)
        elif b == "LM":
            LM_text.set(counter)
            locaterDic["LM"].append(counter)
        elif b == "MM":
            MM_text.set(counter)
            locaterDic["MM"].append(counter)
        elif b == "RM":
            RM_text.set(counter)
            locaterDic["RM"].append(counter)
        elif b == "LB":
            LB_text.set(counter)
            locaterDic["LB"].append(counter)
        elif b == "MB":
            MB_text.set(counter)
            locaterDic["MB"].append(counter)
        elif b == "RB":
            RB_text.set(counter)
            locaterDic["RB"].append(counter)
        counter = "x"

    win()
    print(locaterDic)

def win():
    winLIST = [["LT", "MT", "RT"], ["LM", "MM", "RM"], ["LB", "MB", "RB"], ["LT", "LM", "LB"], ["MT", "MM", "MB"], ["RT", "RM", "RB"], ["LT", "MM", "RB"], ["RT", "MM", "LB"]]
    print(locaterDic["LT"])
    # if locaterDic["LT"] == ['x']:
    #     print("sortaWin")
    for i in winLIST:
        if locaterDic[i[0]] == ['o'] and locaterDic[i[1]] == ['o'] and locaterDic[i[2]] == ['o']:
            print("win")
            winMessage("o")
        elif locaterDic[i[0]] == ['x'] and locaterDic[i[1]] == ['x'] and locaterDic[i[2]] == ['x']:
            print("win")

            winMessage("x")
            
def winMessage(team):

    def close():
        errWin.destroy()
        

    errWin = tk.Toplevel()
    errWin.wm_title("Window")

    l = tk.Label(errWin, text="WIN " + team)
    l.grid(row=0, column=0)

    b = tk.Button(errWin, text="Okay", command = close)
    b.grid(row=1, column=0)
    
LT_text = tk.StringVar()
MT_text = tk.StringVar()
RT_text = tk.StringVar()
LM_text = tk.StringVar()
MM_text = tk.StringVar()
RM_text = tk.StringVar()
LB_text = tk.StringVar()
MB_text = tk.StringVar()
RB_text = tk.StringVar()

myFont = font.Font(size=30)

LT = tk.Button(root, textvariable=LT_text, font = myFont, height = 1, width = 3, command= lambda: Change("LT"))
MT = tk.Button(root, textvariable=MT_text, font = myFont, height = 1, width = 3, command= lambda: Change("MT"))
RT = tk.Button(root, textvariable=RT_text, font = myFont, height = 1, width = 3, command= lambda: Change("RT"))
LM = tk.Button(root, textvariable=LM_text, font = myFont, height = 1, width = 3, command= lambda: Change("LM"))
MM = tk.Button(root, textvariable=MM_text, font = myFont, height = 1, width = 3, command= lambda: Change("MM"))
RM = tk.Button(root, textvariable=RM_text, font = myFont, height = 1, width = 3, command= lambda: Change("RM"))
LB = tk.Button(root, textvariable=LB_text, font = myFont, height = 1, width = 3, command= lambda: Change("LB"))
MB = tk.Button(root, textvariable=MB_text, font = myFont, height = 1, width = 3, command= lambda: Change("MB"))
RB = tk.Button(root, textvariable=RB_text, font = myFont, height = 1, width = 3, command= lambda: Change("RB"))
LT.pack()

LT.grid(row=0, column=0)
MT.grid(row=0, column=1)
RT.grid(row=0, column=2)
LM.grid(row=1, column=0)
MM.grid(row=1, column=1)
RM.grid(row=1, column=2)
LB.grid(row=2, column=0)
MB.grid(row=2, column=1)
RB.grid(row=2, column=2)

# MT.pack()


root.mainloop()