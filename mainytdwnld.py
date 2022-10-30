import rumps
from pytube import YouTube
import pyperclip

yt = "/Users/fabianmoorpucar/PycharmProjects/BatteryTaskbar/yt.png"
icon = "/Users/fabianmoorpucar/PycharmProjects/BatteryTaskbar/icon_white.png"


class PomodoroApp(object):
    def __init__(self):
        self.app = rumps.App("YouTube Downloader", None, icon)


    @rumps.clicked("Download Copied URL as MP4")
    def youtube_dl(sender):
        s = pyperclip.paste()
        yt = YouTube(s)
        stream = yt.streams.get_by_itag(140)
        stream.download("/Users/fabianmoorpucar/Documents/Splice/sounds/packs/0 Downloaded Sounds")
        title = yt.title
        rumps.notification("Download Succeeded", "File saved to HDD", f"{title}")

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = PomodoroApp()
    app.run()