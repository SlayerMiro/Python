import os
from tkinter import *

directory = os.getcwd()


def play(file):
    os.startfile(file)

fileList = []
counter = 0
root = Tk()
root.title("Media Player")
numFiles = 0
for file in os.listdir(directory):
    if file.endswith(".mkv") or file.endswith(".mp4"):
        fileList.append(file)
for x in range(0, len(fileList)):
    name = fileList[counter]
    title = Label(root, text=name)
    playButton = Button(root, text="Play", command=lambda name=name : play(name))
    title.grid(row=x, column=0)
    playButton.grid(row=x, column=1)
    counter += 1

root.mainloop()