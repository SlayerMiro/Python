import os

directory = os.getcwd()
print("Enter Title: ")
title = input()
titleLen = len(title)
for file in os.listdir(directory):
    if file.startswith(title):
        os.rename(file, file[:titleLen] + " (TV)" + file[titleLen:])
