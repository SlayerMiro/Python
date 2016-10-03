import requests
import json
import os
import datetime
import os
import os.path
from tkinter import *


def download(url, name):
    time = datetime.datetime.now()
    os.system(
        "livestreamer --twitch-oauth-token 6gko96m7voe5udkye0z1cyz7v01r1j -o D:\Livestreams\\" + name + "-" + str(time.second) + ".mp4 --hls-segment-threads 4 " + url + " best")


root = Tk()
twitch = requests.get("https://api.twitch.tv/kraken/channels/northernlion/videos?limit=5&broadcasts=true", headers={"Client-ID": "jfyy89kdt4zdf64dzmg3zmvt91j6uca"})

api = twitch.json()
for x in range(0, 5):
    url = api['videos'][x]['url']
    date = api['videos'][x]['recorded_at']
    name = "NLSS-" + date[0:10]
    title = Label(root, text=name)
    downloadButton = Button(root, text="Download", command= lambda url=url, name=name, date=date: download(url, name))
    title.grid(row=x, column=0)
    downloadButton.grid(row=x, column=1)


root.mainloop()
