from tkinter import *
from tkinter.messagebox import showinfo

#Global variables
currentLvl = 1
playerMode = 1

root = Tk()
root.title("CrazyPenguin")
root.geometry("1000x675")
canvas = Canvas(root, width=1000, height=675, background="#bde2dd")
canvas.pack()
photo0=PhotoImage(file="penguin.gif")
image0=canvas.create_image(500, 100, image=photo0, tags="img0")
canvas.create_text(500,250,text="Welcome on Crazy Penguin ! ", tags="welcome")
photo1=PhotoImage(file="play.gif")
image1=canvas.create_image(200, 500, image=photo1, tags="img1")
photo2=PhotoImage(file="exit.gif")
image2=canvas.create_image(800, 500, image=photo2, tags="img2")
canvas.create_text(625,25,text="",tags="score")


#This dictonary contains the entire state of the game1.
game1 = {
    'pos': 85,
    'score':1,
    'hammerPower':0,
    'life':0,
    'enter':0,
    'exit':0,
    'moves': [
            ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',
            ' ',' ',' ',' ',' ',' ',' ','W','W','W',' ',' ',
            ' ',' ',' ',' ',' ',' ',' ','W','S','W',' ',' ',
            ' ',' ',' ',' ',' ',' ',' ','W','O','W',' ',' ',
            ' ',' ',' ',' ',' ',' ',' ','W','O','W',' ',' ',
            ' ',' ',' ',' ',' ',' ',' ','W','O','W',' ',' ',
            'W','W','W','W','W','W','W','W','O','W',' ',' ',
            'W','P','O','O','O','O','O','O','O','W',' ',' ',
            'W','W','W','W','W','W','W','W','W','W',' ',' ',
            ' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '
    ]
}

#This dictonary contains the entire state of the game2.
game2 = {
    'pos': 86,
    'score':1,
    'hammerPower':0,
    'life':0,
    'enter':0,
    'exit':0,
    'moves': [
            ' ',' ',' ','W','W','W','W','W','W','W','W','W',
            ' ',' ',' ','W','O','O','O','O','O','O','S','W',
            ' ',' ',' ','W','O','O','O','O','W','W','W','W',
            ' ',' ','W','W','W','W','W','O','W','W','W',' ',
            ' ',' ','W','O','O','W','W','O','O','O','W',' ',
            'W','W','W','O','O','O','W','O','O','O','W',' ',
            'W','O','O','O','O','O','W','W','W','O','W',' ',
            'W','O','P','W','O','O','O','O','O','O','W',' ',
            'W','O','O','W','W','O','O','O','O','W','W',' ',
            'W','W','W','W','W','W','W','W','W','W',' ',' '
    ]
}

#This dictonary contains the entire state of the game3.
game3 = {
    'pos': 119,
    'score':1,
    'hammerPower':0,
    'life':0,
    'enter':50,
    'exit':13,
    'moves': [
            'W','O','O','W','W','O','O','O','C','O','O','W',
            'W','T','O','W','W','O','W','W','C','C','O','W',
            'O','O','O','W','W','O','H','W','C','O','W','W',
            'O','S','W','W','W','O','O','W','O','O','W','W',
            'W','W','T','W','W','O','W','W','O','O','C','O',
            'W','W','O','W','W','W','O','W','C','O','O','C',
            'W','O','O','O','O','O','O','W','W','O','O','W',
            'W','O','O','O','O','O','W','W','W','O','O','C',
            'W','W','O','O','W','W','W','W','W','O','O','O',
            'W','W','W','W','W','W','W','W','W','W','W','P'
    ]
}

#This dictonary contains the entire state of the current game.
game = {
    'pos': 0,
    'score':1,
    'hammerPower':0,
    'life':0,
    'enter':0,
    'exit':0,
    'moves': []
}

def leftKey(event):
    global currentLvl
    global playerMode
    global game
    penguin = game["pos"]
    if game["moves"][penguin-1] != 'W':
        if game["moves"][penguin-1] == 'S':
            game["score"] += 1
            game["moves"][penguin] = 'B'
            game["pos"] -= 1
            game["moves"][penguin-1] = 'P'
            printGame()
            canvas.delete(canvas.find_withtag("result"))
            if playerMode == 1:
                if currentLvl == 1:
                    canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                    currentLvl = 2
                    init()
                    win(0)
                elif currentLvl == 2:
                    canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                    currentLvl = 3
                    init()
                    win(1)
                else:
                    canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                    win(2)
                printGame()
            else:
                if currentLvl == 1:
                    if game["score"] == 13:
                        canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                        currentLvl = 2
                        init()
                        win(0)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                elif currentLvl == 2:
                    if game["score"] == 43:
                        canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                        currentLvl = 3
                        init()
                        win(1)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                else:
                    if game["score"] == 77:
                        canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                        win(2)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                printGame()
        elif game["moves"][penguin-1] == 'B':
            if game["life"] == 1:
                if currentLvl == 1:
                    game = game1
                elif currentLvl == 2:
                    game = game2
                else:
                    game = game3
                game["life"] = 0
                printGame()
            else:
                canvas.delete(canvas.find_withtag("result"))
                canvas.create_text(800,150,text="You Loose...", tags="result")
                retry(0)
        elif game["moves"][penguin-1] == 'C':
            game["score"] +=3
            game["moves"][penguin] = 'B'
            game["pos"] -= 1
            game["moves"][penguin-1] = 'P'
            printGame()
        elif game["moves"][penguin-1] == 'H':
            game["hammerPower"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 1
            game["moves"][penguin-1] = 'P'
            printGame()
        elif game["moves"][penguin-1] == 'G':
            game["life"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 1
            game["moves"][penguin-1] = 'P'
            printGame()
        elif game["moves"][penguin-1] == 'T':
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] = game3["exit"]
            game["moves"][game3["exit"]] = 'P'
            printGame()
        else:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 1
            game["moves"][penguin-1] = 'P'
            printGame()
    else:
        if game["hammerPower"] == 1:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 1
            game["moves"][penguin-1] = 'P'
            game["hammerPower"] = 0
            printGame() 
        else:
            print("hammerPower : 0")        

def rightKey(event):
    global currentLvl
    global playerMode
    global game
    penguin = game["pos"]
    if game["moves"][penguin+1] != 'W':
        if game["moves"][penguin+1] == 'S':
            game["score"] += 1
            game["moves"][penguin] = 'B'
            game["pos"] += 1
            game["moves"][penguin+1] = 'P'
            printGame()
            canvas.delete(canvas.find_withtag("result"))
            if playerMode == 1:
                if currentLvl == 1:
                    canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                    currentLvl = 2
                    init()
                    win(0)
                elif currentLvl == 2:
                    canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                    currentLvl = 3
                    init()
                    win(1)
                else:
                    canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                    win(2)
                printGame()
            else:
                if currentLvl == 1:
                    if game["score"] == 13:
                        canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                        currentLvl = 2
                        init()
                        win(0)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                elif currentLvl == 2:
                    if game["score"] == 43:
                        canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                        currentLvl = 3
                        init()
                        win(1)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                else:
                    if game["score"] == 77:
                        canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                        win(2)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                printGame()
        elif game["moves"][penguin+1] == 'B':
            if game["life"] == 1:
                if currentLvl == 1:
                    game = game1
                elif currentLvl == 2:
                    game = game2
                else:
                    game = game3
                game["life"] = 0
                printGame()
            else:
                canvas.delete(canvas.find_withtag("result"))
                canvas.create_text(800,150,text="You Loose...", tags="result")
                retry(0)
        elif game["moves"][penguin+1] == 'C':
            game["score"] +=3
            game["moves"][penguin] = 'B'
            game["pos"] += 1
            game["moves"][penguin+1] = 'P'
            printGame()
        elif game["moves"][penguin+1] == 'H':
            game["hammerPower"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 1
            game["moves"][penguin+1] = 'P'
            printGame()
        elif game["moves"][penguin+1] == 'G':
            game["life"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 1
            game["moves"][penguin+1] = 'P'
            printGame()
        elif game["moves"][penguin+1] == 'T':
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] = game3["exit"]
            game["moves"][game3["exit"]] = 'P'
            printGame()
        else:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 1
            game["moves"][penguin+1] = 'P'
            printGame()
    else:
        if game["hammerPower"] == 1:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 1
            game["moves"][penguin+1] = 'P'
            game["hammerPower"] = 0
            printGame() 
        else:
            print("hammerPower : 0")

def upKey(event):
    global currentLvl
    global playerMode
    global game
    penguin = game["pos"]
    if game["moves"][penguin-12] != 'W':
        if game["moves"][penguin-12] == 'S':
            game["score"] += 1
            game["moves"][penguin] = 'B'
            game["pos"] -= 12
            game["moves"][penguin-12] = 'P'
            printGame()
            canvas.delete(canvas.find_withtag("result"))
            if playerMode == 1:
                if currentLvl == 1:
                    canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                    currentLvl = 2
                    init()
                    win(0)
                elif currentLvl == 2:
                    canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                    currentLvl = 3
                    init()
                    win(1)
                else:
                    canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                    win(2)
                printGame()
            else:
                if currentLvl == 1:
                    if game["score"] == 13:
                        canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                        currentLvl = 2
                        init()
                        win(0)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                elif currentLvl == 2:
                    if game["score"] == 43:
                        canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                        currentLvl = 3
                        init()
                        win(1)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                else:
                    if game["score"] == 77:
                        canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                        win(2)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                printGame()
        elif game["moves"][penguin-12] == 'B':
            if game["life"] == 1:
                if currentLvl == 1:
                    game = game1
                elif currentLvl == 2:
                    game = game2
                else:
                    game = game3
                game["life"] = 0
                printGame()
            else:
                canvas.delete(canvas.find_withtag("result"))
                canvas.create_text(800,150,text="You Loose...", tags="result")
                retry(0)
        elif game["moves"][penguin-12] == 'C':
            game["score"] +=3
            game["moves"][penguin] = 'B'
            game["pos"] -= 12
            game["moves"][penguin-12] = 'P'
            printGame()
        elif game["moves"][penguin-12] == 'H':
            game["hammerPower"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 12
            game["moves"][penguin-12] = 'P'
            printGame()
        elif game["moves"][penguin-12] == 'G':
            game["life"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 12
            game["moves"][penguin-12] = 'P'
            printGame()
        elif game["moves"][penguin-12] == 'T':
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] = game3["exit"]
            game["moves"][game3["exit"]] = 'P'
            printGame()
        else:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 12
            game["moves"][penguin-12] = 'P'
            printGame()
    else:
        if game["hammerPower"] == 1:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] -= 12
            game["moves"][penguin-12] = 'P'
            game["hammerPower"] = 0
            printGame() 
        else:
            print("hammerPower : 0")

def downKey(event):
    global currentLvl
    global playerMode
    global game
    penguin = game["pos"]
    if game["moves"][penguin+12] != 'W':
        if game["moves"][penguin+12] == 'S':
            game["score"] += 1
            game["moves"][penguin] = 'B'
            game["pos"] += 12
            game["moves"][penguin+12] = 'P'
            printGame()
            canvas.delete(canvas.find_withtag("result"))
            if playerMode == 1:
                if currentLvl == 1:
                    canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                    currentLvl = 2
                    init()
                    win(0)
                elif currentLvl == 2:
                    canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                    currentLvl = 3
                    init()
                    win(1)
                else:
                    canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                    win(2)
                #printGame()
            else:
                if currentLvl == 1:
                    if game["score"] == 13:
                        canvas.create_text(800,150,text="You Win ! Level 2 now !", tags="result")
                        currentLvl = 2
                        init()
                        win(0)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                elif currentLvl == 2:
                    if game["score"] == 43:
                        canvas.create_text(800,150,text="You Win ! Level 3 now !", tags="result")
                        currentLvl = 3
                        init()
                        win(1)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                else:
                    if game["score"] == 77:
                        canvas.create_text(800,150,text="You Win ! Congratulations !", tags="result")
                        win(2)
                    else:
                        canvas.create_text(800,150,text="You Loose... Read above...", tags="result")
                        retry(1)
                printGame()
        elif game["moves"][penguin+12] == 'B':
            if game["life"] == 1:
                if currentLvl == 1:
                    game = game1
                elif currentLvl == 2:
                    game = game2
                else:
                    game = game3
                game["life"] = 0
                printGame()
            else:
                canvas.delete(canvas.find_withtag("result"))
                canvas.create_text(800,150,text="You Loose...", tags="result")
                retry(0)
        elif game["moves"][penguin+12] == 'C':
            game["score"] +=3
            game["moves"][penguin] = 'B'
            game["pos"] += 12
            game["moves"][penguin+12] = 'P'
            printGame()
        elif game["moves"][penguin+12] == 'H':
            game["hammerPower"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 12
            game["moves"][penguin+12] = 'P'
            printGame()
        elif game["moves"][penguin+12] == 'G':
            game["life"] = 1
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 12
            game["moves"][penguin+12] = 'P'
            printGame()
        elif game["moves"][penguin+12] == 'T':
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] = game3["exit"]
            game["moves"][game3["exit"]] = 'P'
            printGame()
        else:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 12
            game["moves"][penguin+12] = 'P'
            printGame()
    else:
        if game["hammerPower"] == 1:
            game["score"] +=1
            game["moves"][penguin] = 'B'
            game["pos"] += 12
            game["moves"][penguin+12] = 'P'
            game["hammerPower"] = 0
            printGame() 
        else:
            print("hammerPower : 0")

def init():
    global currentLvl
    global game
    if currentLvl == 1:
        game = game1
    elif currentLvl == 2:
        game = game2
    else:
        game = game3

def cleaner(event):
    init()
    canvas.delete("mode1")
    canvas.delete("mod1")
    canvas.delete("mode2")
    canvas.delete("mod2")
    canvas.delete("result")
    printGame()

def click(event):
    canvas.delete(canvas.find_withtag("img1"))
    canvas.delete(canvas.find_withtag("img2"))
    canvas.delete(canvas.find_withtag("welcome"))
    selectMode()

def exit(event):
    print("exit function")
    root.destroy()
    print("click sur exit")

def setMode1(event):
    global playerMode
    playerMode = 1
    canvas.delete(canvas.find_withtag("img0"))
    canvas.delete(canvas.find_withtag("welcome"))
    canvas.delete(canvas.find_withtag("info1"))
    canvas.delete(canvas.find_withtag("info2"))
    canvas.delete(canvas.find_withtag("mode1"))
    canvas.delete(canvas.find_withtag("mode2"))
    canvas.delete(canvas.find_withtag("mod1"))
    canvas.delete(canvas.find_withtag("mod2"))
    printGame()

def setMode2(event):
    global playerMode
    playerMode = 2
    #print("playerMode 2 : "+str(playerMode))
    canvas.delete(canvas.find_withtag("img0"))
    canvas.delete(canvas.find_withtag("welcome"))
    canvas.delete(canvas.find_withtag("info1"))
    canvas.delete(canvas.find_withtag("info2"))
    canvas.delete(canvas.find_withtag("mode1"))
    canvas.delete(canvas.find_withtag("mode2"))
    canvas.delete(canvas.find_withtag("mod1"))
    canvas.delete(canvas.find_withtag("mod2"))
    printGame()
    

def selectMode():
    canvas.create_text(500,250,text="Ok now chose your mode : ", tags="welcome")
    canvas.create_text(500,500,text="Mode 1 : You just have to pass the level ", tags="info1")
    canvas.create_text(500,550,text="Mode 2 : You have to pass the level by passing on all the squares ", tags="info2")
    mod1 = canvas.create_rectangle(50,500,200,600, tags="mode1", fill="blue")
    txtmod1 = canvas.create_text(125,550,text="Mode 1 ", tags="mod1")
    mod2 = canvas.create_rectangle(800,500,950,600, tags="mode2", fill="blue")
    txtmod2 = canvas.create_text(875,550,text="Mode 2 ", tags="mod2")
    canvas.tag_bind(mod1, '<1>', setMode1)
    canvas.tag_bind(mod2, '<1>', setMode2)
    canvas.tag_bind(txtmod1, '<1>', setMode1)
    canvas.tag_bind(txtmod2, '<1>', setMode2)

def retry(x):
    canvas.delete("all")
    if x == 0:
        canvas.create_text(500,250,text="You Loose... Seriously..? You can not play anymore... Quit ! ", tags="welcome")
    else:
        canvas.create_text(500,250,text="You Loose... You have to pass on all the squares... Seriously..? You can not play anymore... Quit ! ", tags="welcome")
    print("before mod2")
    mod2 = canvas.create_rectangle(800,500,950,600, tags="mode2", fill="blue")
    txtmod2 = canvas.create_text(875,550,text=" Quit ", tags="mod2")
    print("before bind")
    canvas.tag_bind(mod2, '<1>', exit)
    canvas.tag_bind(txtmod2, '<1>', exit)
    print("after bind")
    root.mainloop()

def win(x):
    canvas.delete("all")
    if x == 0:
        canvas.create_text(500,250,text="You Win ! Level 2 now !", tags="welcome")
        mod1 = canvas.create_rectangle(50,500,200,600, tags="mode1", fill="blue")
        txtmod1 = canvas.create_text(125,550,text=" Yes  ", tags="mod1")
        canvas.tag_bind(mod1, '<1>', cleaner)
        canvas.tag_bind(txtmod1, '<1>', cleaner)
    elif x == 1:
        canvas.create_text(500,250,text="You Win ! Level 3 now !", tags="welcome")
        mod1 = canvas.create_rectangle(50,500,200,600, tags="mode1", fill="blue")
        txtmod1 = canvas.create_text(125,550,text=" Yes  ", tags="mod1")
        canvas.tag_bind(mod1, '<1>', cleaner)
        canvas.tag_bind(txtmod1, '<1>', cleaner)
    else:
        canvas.create_text(500,250,text="You Finish the Game ! Congratulations !", tags="welcome")
    
    mod2 = canvas.create_rectangle(800,500,950,600, tags="mode2", fill="blue")
    txtmod2 = canvas.create_text(875,550,text=" Quit ", tags="mod2")
    canvas.tag_bind(mod2, '<1>', exit)
    canvas.tag_bind(txtmod2, '<1>', exit)
    root.mainloop()

root.bind("<Left>", leftKey)
root.bind("<Right>", rightKey)
root.bind("<Up>", upKey)
root.bind("<Down>", downKey)
canvas.tag_bind(image1, '<1>', click)
canvas.tag_bind(image2, '<1>', exit)


def printGame():
    global currentLvl
    global game
    canvas.delete(canvas.find_withtag("score"))
    canvas.delete(canvas.find_withtag("level"))
    canvas.delete(canvas.find_withtag("info"))
    canvas.delete(canvas.find_withtag("info1"))
    canvas.delete(canvas.find_withtag("info2"))
    canvas.delete(canvas.find_withtag("legend1"))
    canvas.delete(canvas.find_withtag("legend2"))
    canvas.delete(canvas.find_withtag("legend3"))
    canvas.delete(canvas.find_withtag("legend4"))
    canvas.create_rectangle(700, 150, 750, 200, fill="green")
    canvas.create_text(800,175,text="Penguin", tags="legend1")
    canvas.create_rectangle(700, 200, 750, 250, fill="white")
    canvas.create_text(800,225,text="Ice Square", tags="legend2")
    canvas.create_rectangle(700, 250, 750, 300, fill="blue")
    canvas.create_text(800,275,text="Water", tags="legend3")
    canvas.create_rectangle(700, 300, 750, 350, fill="red")
    canvas.create_text(800,325,text="Exit Square", tags="legend4")

    if currentLvl == 1:
        canvas.create_text(75,25,text="Level 1", tags="level")
        Score = canvas.create_text(625,25,text=str(game["score"]) + " / 13", tags="score")
    elif currentLvl == 2:
        canvas.create_text(75,25,text="Level 2", tags="level")
        Score = canvas.create_text(625,25,text=str(game["score"]) + " / 43", tags="score")
    else:
        canvas.create_text(75,25,text="Level 3", tags="level")
        Score = canvas.create_text(625,25,text=str(game["score"]) + " / 81", tags="score")
        canvas.delete(canvas.find_withtag("legend5"))
        canvas.delete(canvas.find_withtag("legend6"))
        canvas.delete(canvas.find_withtag("legend7"))
        canvas.create_rectangle(700, 350, 750, 400, fill="gold")
        canvas.create_text(800,375,text="Coin", tags="legend5")
        canvas.create_rectangle(700, 400, 750, 450, fill="orange")
        canvas.create_text(800,425,text="Hammer", tags="legend6")
        canvas.create_rectangle(700, 450, 750, 500, fill="brown")
        canvas.create_text(800,475,text="Tunnel", tags="legend7")
    if playerMode == 1:
        Info = canvas.create_text(800,75,text="You just have to finish the level", tags="info")
    else:
        Info1 = canvas.create_text(800,75,text="You have to pass throught all the squares", tags="info1")
        Info2 = canvas.create_text(800,100,text="to validate the level", tags="info2")
    
    column = 50
    line = 50
    iterator = 0
    for i in game["moves"]:
        if column == 650:
            line+=50
            column = 50
            if i == ' ':
                canvas.create_rectangle(column, line, column+50, line+50, fill="grey", tags=iterator)
            elif i == 'W':
                canvas.create_rectangle(column, line, column+50, line+50, fill="black", tags=iterator)
            elif i == 'C':
                canvas.create_rectangle(column, line, column+50, line+50, fill="gold", tags=iterator)
            elif i == 'H':
                canvas.create_rectangle(column, line, column+50, line+50, fill="orange", tags=iterator)
            elif i == 'G':
                canvas.create_rectangle(column, line, column+50, line+50, fill="purple", tags=iterator)
            elif i == 'T':
                canvas.create_rectangle(column, line, column+50, line+50, fill="brown", tags=iterator)
            elif i == 'O':
                canvas.create_rectangle(column, line, column+50, line+50, fill="white", tags=iterator)
            elif i == 'B':
                canvas.create_rectangle(column, line, column+50, line+50, fill="blue", tags=iterator)
            elif i == 'P':
                '''photo=PhotoImage(file="pgn2.gif")
                image0=canvas.create_image(800, 150, image=photo, tags=iterator)
                root.mainloop()'''
                canvas.create_rectangle(column, line, column+50, line+50, fill="green", tags=iterator)
            elif i == 'S':
                canvas.create_rectangle(column, line, column+50, line+50, fill="red", tags=iterator)
        else:
            if i == ' ':
                canvas.create_rectangle(column, line, column+50, line+50, fill="grey", tags=iterator)
            elif i == 'W':
                canvas.create_rectangle(column, line, column+50, line+50, fill="black", tags=iterator)
            elif i == 'C':
                canvas.create_rectangle(column, line, column+50, line+50, fill="gold", tags=iterator)
            elif i == 'H':
                canvas.create_rectangle(column, line, column+50, line+50, fill="orange", tags=iterator)
            elif i == 'T':
                canvas.create_rectangle(column, line, column+50, line+50, fill="brown", tags=iterator)
            elif i == 'G':
                canvas.create_rectangle(column, line, column+50, line+50, fill="purple", tags=iterator)
            elif i == 'O':
                canvas.create_rectangle(column, line, column+50, line+50, fill="white", tags=iterator)
            elif i == 'B':
                canvas.create_rectangle(column, line, column+50, line+50, fill="blue", tags=iterator)
            elif i == 'P':
                '''photo=PhotoImage(file="pgn2.gif")
                image0=canvas.create_image(800, 150, image=photo, tags=iterator)
                root.mainloop()'''
                canvas.create_rectangle(column, line, column+50, line+50, fill="green", tags=iterator)
            elif i == 'S':
                canvas.create_rectangle(column, line, column+50, line+50, fill="red", tags=iterator)
        column+=50
        iterator+=1 


def main():
    init()
    root.mainloop()


if __name__ == "__main__":
    main()

