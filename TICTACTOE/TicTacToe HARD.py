import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.minsize(250, 100)
root.title("TicTacToe")
counter = "x"
locaterDic = {"LT":[],"MT":[],"RT":[],"LM":[],"MM":[],"RM":[],"LB":[],"MB":[],"RB":[]}
winLIST = [["LT", "MT", "RT"], ["LM", "MM", "RM"], ["LB", "MB", "RB"], ["LT", "LM", "LB"], ["MT", "MM", "MB"], ["RT", "RM", "RB"], ["LT", "MM", "RB"], ["RT", "MM", "LB"]]
awin = [["LT", "MT"], ["LT","RT"], ["MT", "RT"], ["LM", "MM"], ["LM", "RM"], ["MM", "RM"], ["LB", "MB"], ["LB", "RB"], ["MB", "RB"], ["LT", "LM"], ["LT", "LB"], ["LM", "LB"], ["MT", "MM"], ["MT""MB"], ["MM", "MB"], ["RT", "RM"], ["RT", "RB"], ["RM", "RB"], ["LT", "MM"], ["LT", "RB"],  ["MM", "RB"], ["RT", "MM"], ["RT", "LB"], ["MM", "LB"]]

def Change(b, counter):
    
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

def MainF(b):
    global counter
    
    
    if counter == "x":
        Change(b, counter)

        counter = "x"
    else:

        Change(b, counter)
        counter = "x"
    cpu()
    win()

def win():
    for i in winLIST:
        if locaterDic[i[0]] == ['o'] and locaterDic[i[1]] == ['o'] and locaterDic[i[2]] == ['o']:
            gameMessage("O")
        elif locaterDic[i[0]] == ['x'] and locaterDic[i[1]] == ['x'] and locaterDic[i[2]] == ['x']:
            gameMessage("X")

def cpu():
    notRUN = False
    xpos = []
    for i in locaterDic:
        if locaterDic[i] == ['x']:
            xpos.append(i)
    for pat in awin:
        if all(letter in xpos for letter in pat):
            for i in winLIST:
                if pat[0] in str(i) and pat[1] in str(i):
                    i.remove(pat[0])
                    i.remove(pat[1])
                    i = str(i).replace("[", "").replace("]", "").replace("'", "")
                    if notRUN is False:
                        if locaterDic[i] == []:
                            notRUN = True
                            Change(i, "o")
                            break
                    
    if notRUN is False:
        for i in locaterDic:
            if locaterDic[i] == []: 
                Change(i, "o")
                break


def gameMessage(team):

    def close():
        Message.destroy()
        

    Message = tk.Toplevel()
    Message.wm_title("Window")

    l = tk.Label(Message, text=team + " Has Won!")
    l.grid(row=0, column=0)

    b = tk.Button(Message, text="Okay", command = close)
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

LT = tk.Button(root, textvariable=LT_text, font = myFont, height = 1, width = 3, command= lambda: MainF("LT"))
MT = tk.Button(root, textvariable=MT_text, font = myFont, height = 1, width = 3, command= lambda: MainF("MT"))
RT = tk.Button(root, textvariable=RT_text, font = myFont, height = 1, width = 3, command= lambda: MainF("RT"))
LM = tk.Button(root, textvariable=LM_text, font = myFont, height = 1, width = 3, command= lambda: MainF("LM"))
MM = tk.Button(root, textvariable=MM_text, font = myFont, height = 1, width = 3, command= lambda: MainF("MM"))
RM = tk.Button(root, textvariable=RM_text, font = myFont, height = 1, width = 3, command= lambda: MainF("RM"))
LB = tk.Button(root, textvariable=LB_text, font = myFont, height = 1, width = 3, command= lambda: MainF("LB"))
MB = tk.Button(root, textvariable=MB_text, font = myFont, height = 1, width = 3, command= lambda: MainF("MB"))
RB = tk.Button(root, textvariable=RB_text, font = myFont, height = 1, width = 3, command= lambda: MainF("RB"))

LT.grid(row=0, column=0)
MT.grid(row=0, column=1)
RT.grid(row=0, column=2)
LM.grid(row=1, column=0)
MM.grid(row=1, column=1)
RM.grid(row=1, column=2)
LB.grid(row=2, column=0)
MB.grid(row=2, column=1)
RB.grid(row=2, column=2)

root.mainloop()