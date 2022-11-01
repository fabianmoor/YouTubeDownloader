import rumps
from pytube import YouTube
import pyperclip
from tkinter import filedialog
from tkinter import *

# Not sure TBH, just initialize window for tkinter
root = Tk()
root.withdraw()

# Icon
icon = "/Users/fabianmoorpucar/PycharmProjects/BatteryTaskbar/icon_white.png"


# App Class
class PomodoroApp(object):
    def __init__(self):
        self.app = rumps.App("YouTube Downloader", None, icon)

    @rumps.clicked("Download Copied URL as MP4")
    def youtube_dl(sender):
        # Ask for destination for file
        userdir = filedialog.asksaveasfilename()

        # Separate directory list by "/" in order to fetch filename
        filelist = userdir.split("/")

        # Define last index in separated list
        filename = filelist[-1]

        # Define number of letters
        count = len(filename) + 1

        # Define destination by removing last folder name from dir -1 "/"
        destination = userdir[:-count]

        if userdir != "":
            # Saving clip board copied url into variable "s"
            s = pyperclip.paste()

            # Transferring clip board url into YouTube
            yt = YouTube(s)

            # Fetch the right format & bitrate for file format (mp4)
            stream = yt.streams.get_by_itag(140)

            # Directory to save file
            stream.download(destination, filename=filename + ".mp4")

            # Fetch YouTube video title
            title = filename

            # Notification for succeeded or failed download
            rumps.notification("Download Succeeded", f"File saved to {destination}", f"{title}")

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = PomodoroApp()
    app.run()
