#!/usr/bin/python
import subprocess as sp
import time
import os
from pirDetect import *
import sys

video = ["omxplayer", "filename", "-o", "both", "--win", "0 0 1280 720", "--aspect-mode", "fill", "--no-osd", "--orientation" ,"180","--vol", "-600"]
scareFile = "/home/pi/Projects/Halloween/ScareMedia/{0}ScareV.mp4".format(sys.argv[1])
print(scareFile)

def onMotion(currState):
    if currState:
        video[1] = scareFile
        subVideo = sp.Popen(video)
        while subVideo.poll() is None:
            time.sleep(.1)


def showImage():
    os.system("sudo fbi -T 1 -d /dev/fb0 -noverbose -once /home/pi/Projects/Halloween/ScareMedia/{0}Start.png".format(
        sys.argv[1]))


showImage()
objDetect = detector(7)
objDetect.subscribe(onMotion)
objDetect.start()
os.system("sudo killall -9 fbi")
