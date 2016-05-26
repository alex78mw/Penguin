from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

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
            print("hammerPower : 0")}
