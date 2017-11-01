import requests
import json
import os
import datetime
import os
import os.path
from tkinter import *


def download(new_url, name):
    time = datetime.datetime.now()
    directory = os.getcwd()
    os.system(
        "streamlink --twitch-oauth-token=n3qqe95xrq5b17hopk73jxj91ahy8o -o " + directory + "\\" + name + "-" + str(time.second) + ".mp4 --hls-segment-threads 4 " + new_url + " best")

def VODs(self):
    n = int(selector.get())
    twitch = requests.get("https://api.twitch.tv/kraken/channels/northernlion/videos?limit=" + str(n) + "&broadcasts=true", headers={'Client-ID': 'jfyy89kdt4zdf64dzmg3zmvt91j6uca', 'Authorization': 'OAuth n3qqe95xrq5b17hopk73jxj91ahy8o' ,'Accept': 'application/vnd.twitchtv.v3+json'})
    api = twitch.json()
    for x in range(0, n):
        url = api['videos'][x]['url']
        new_url = url  # url[:29] + 'videos/' + url[29:]
        date = api['videos'][x]['recorded_at']
        name = "NLSS-" + date[0:10]
        title = Label(root, text=name)
        downloadButton = Button(root, text="Download", command= lambda new_url=new_url, name=name, date=date: download(new_url, name))
        title.grid(row=x+1, column=0)
        downloadButton.grid(row=x+1, column=1)

root = Tk()
root.title("NLSS Downloader")
selector = StringVar(root)
selector.set("5")
dropdownName = Label(root, text="Number of VODs")
dropdownName.grid(row=0, column=0)
w = OptionMenu(root, selector, "5", "10", command=VODs)
w.grid(row=0, column=1)
VODs(self=1)
root.mainloop()
