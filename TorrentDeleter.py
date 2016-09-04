import os

directory = os.getcwd()

for file in os.listdir(directory):
    if file.endswith(".torrent"):
        os.remove(file)

