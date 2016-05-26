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
}