import cv2
import numpy as np
import sys
import os
import threading
import time
import vlc
import easygui

def playVideoA():
    Instance = vlc.Instance('--fullscreen')
    player = Instance.media_player_new()
    Media = Instance.media_new('F:\\Downloads\\[HorribleSubs] 91 Days - 13 [720p].mkv')
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    while True:
        time.sleep(5)
        player.stop()
    print('Finished Video\n')

def playVideoB():
    Instance = vlc.Instance('--fullscreen')
    player = Instance.media_player_new()
    Media = Instance.media_new('C:\\Users\\thunderstruck\\Videos\\test.mp4')
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    while True:
        time.sleep(5)
        player.stop()
    print('Finished Video\n')

def eyeTrack():
    print("Starting eyetrack\n")
    time.sleep(5)
    print("Finishing eyetrack\n")
    return True

if __name__ == "__main__":
    print("Starting program")
    vidThread = threading.Thread(target=eyeTrack)
    vidThread.start()
    if eyeTrack() == True:
        playVideoA()
    else:
        playVideoB()


