import tkinter as tk
import tkinter.font as font

root = tk.Tk()
root.minsize(250, 100)
root.title("TicTacToe")
counter = "x"
locaterDic = {"LT":[],"MT":[],"RT":[],"LM":[],"MM":[],"RM":[],"LB":[],"MB":[],"RB":[]}

def MainF(b, counter):
    
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

def Change(b):
    global counter
    
    
    if counter == "x":
        MainF(b, counter)

        counter = "x"
    else:

        MainF(b, counter)
        counter = "x"
    cpu()
    win()

def win():
    winLIST = [["LT", "MT", "RT"], ["LM", "MM", "RM"], ["LB", "MB", "RB"], ["LT", "LM", "LB"], ["MT", "MM", "MB"], ["RT", "RM", "RB"], ["LT", "MM", "RB"], ["RT", "MM", "LB"]]
    for i in winLIST:
        if locaterDic[i[0]] == ['o'] and locaterDic[i[1]] == ['o'] and locaterDic[i[2]] == ['o']:
            print("win")
            winMessage("o")
        elif locaterDic[i[0]] == ['x'] and locaterDic[i[1]] == ['x'] and locaterDic[i[2]] == ['x']:
            print("win")

            winMessage("x")


def cpuCorners(status):
    corners = ['LT', 'RT', 'RB', 'LB']
    print(status)
    notRUN = False
    if status is False:
        for i in corners:
            if locaterDic[i] == []:
                locaterDic[i].append("o")
                if i == "LT":
                    LT_text.set("o")
                    notRUN = True
                elif i == "RT":
                    RT_text.set("o")
                    notRUN = True
                elif i == "LB":
                    LB_text.set("o")
                    notRUN = True
                elif i == "RB":
                    RB_text.set("o")
                    notRUN = True
    if notRUN is False:
        for i in locaterDic:
            print(locaterDic[i])
            if locaterDic[i] == []: 
                MainF(i, "o")
                break

def cpu():
    count = 0
    notRUN = False
    corners = ['LT', 'RT', 'RB', 'LB']
    for i in corners:
        if str(locaterDic).count("o") < 2:
            print(locaterDic[i])
            if locaterDic[i] == []:
                locaterDic[i].append("o")
                if i == "LT":
                    LT_text.set("o")
                    notRUN = True
                elif i == "RT":
                    RT_text.set("o")
                    notRUN = True
                elif i == "RB":
                    print("RU")
                    RB_text.set("o")
                    notRUN = True
                elif i == "LB":
                    print("LEFT BOTTM")
                    LB_text.set("o")
                    notRUN = True                    
                break
    
    if notRUN == False:
        
        if str(locaterDic).count("o") > 1:
            for i in corners:
                if locaterDic[i] == ['o']:

                    if i == "RT":
                        if locaterDic["MT"] == []:
                            MT_text.set("o")
                            locaterDic["MT"].append("o")
                            notRUN = True
                        else:
                            if notRUN is False:
                                cpuCorners(notRUN)
                                break
                    elif i == "RB":
                        if locaterDic["RM"] == []:
                            RM_text.set("o")
                            locaterDic["RM"].append("o")
                            notRUN = True
                        else:
                            if notRUN is False:
                                cpuCorners(notRUN)
                                break
                    elif i == "LB":
                        if locaterDic["MB"] == []:
                            MB_text.set("o")
                            locaterDic["MB"].append("o")
                            notRUN = True
                        else:
                            if notRUN is False:
                                cpuCorners(notRUN)
                                break
                    elif i == "RB":
                        if locaterDic["LM"] == []:
                            LM_text.set("o")
                            locaterDic["LM"].append("o")
                            notRUN = True
                        else:
                            if notRUN is False:
                                cpuCorners(notRUN)
                                break
        
                    

    




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