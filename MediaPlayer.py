import os
from tkinter import *

directory = os.getcwd()


def play(file):
    os.startfile(file)

root = Tk()
numFiles = 0
for file in os.listdir(directory):
    if file.endswith(".mkv") or file.endswith(".mp4"):
        numFiles += 1

for x in range(0, numFiles):
    for file in os.listdir(directory):
        if file.endswith(".mkv") or file.endswith(".mp4"):
            name = file
            print(name)
            title = Label(root, text=name)
            playButton = Button(root, text="Play", command= lambda file=file: play(file))
            title.grid(row=x, column=0)
            playButton.grid(row=x, column=1)

root.mainloop()