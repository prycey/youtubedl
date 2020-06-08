import eel
from pytube import YouTube
import os
import subprocess
import time
import sys



eel.init('web')

@eel.expose
def download(url, user):
    print(url)
    while True:
        # Title and Time
        print("...")
        print((YouTube(url)).title)
        print("...")

        # Filename specification
        # Prevents any errors during conversion due to illegal characters in name
        _filename = url
        dirs = "C:\\Users\\"
        dirs2 = "\\Downloads"
        path = [dirs,user,dirs2]
        # Downloading
        print("Downloading....")
        YouTube(url).streams.first().download(filename=_filename, output_path = ''.join(path))
        time.sleep(1)

        # Converting
        mp4 = "'%s'.mp4" % _filename
        mp3 = "'%s'.mp3" % _filename
        ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
        subprocess.call(ffmpeg, shell=True)

        # Completion
        print("\nCOMPLETE\n")
        break

eel.start('youtubedlapp.html', block=False)

while True:
    eel.sleep(10)
