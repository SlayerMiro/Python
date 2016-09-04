import os

directory = os.getcwd()

for file in os.listdir(directory):
    if file.endswith(".torrent"):
        os.remove(file)
    elif file.endswith(".exe") or file.endswith(".zip") or file.endswith(".rar"):
        print(file)
        print("Do you want to delete this? y/n/ya/na")
        answer = str(input())
        if answer is "ya":
            for file in os.listdir() file.endswith(".exe") is True:
                os.remove(file)
