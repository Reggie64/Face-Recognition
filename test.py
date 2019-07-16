import cv2
import numpy as np
import sys
import os
from moviepy.editor import *
import pygame


vidSource = "F:\\Downloads\\[HorribleSubs] 91 Days - 13 [720p].mkv"
graphicVid = "F:\\Downloads\\[HorribleSubs] 91 Days - 13 [720p].mkv"
eyeCapture = True
#def faceRecognize():


def playVideo(vidSource, eyeCapture):
    pygame.init()
    pygame.display.set_caption('Face')
    infoObject = pygame.display.Info()
    display_width = infoObject.current_w
    display_height = infoObject.current_h
    vidDisplay = pygame.display.set_mode((display_width, display_height))

    clip = VideoFileClip(vidSource)
    graphicClip = VideoFileClip(graphicVid)

    if eyeCapture == True:
        clip.preview()
    elif eyeCapture == False:
        graphicClip.preview()

    pygame.quit()

if __name__ == "__main__":
    #faceRecognize()
    playVideo(vidSource, eyeCapture)