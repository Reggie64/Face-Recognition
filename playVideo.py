import cv2
import numpy as np
from moviepy.editor import *
import pygame


vidSource = "F:\\Downloads\\[HorribleSubs] Fairy Tail Final Season - 311 [720p].mkv"

def faceRecognize():


def playVideo(vidSource):
    pygame.display.set_caption('Hello World!')

    clip = VideoFileClip(vidSource)
    clip.preview()

    pygame.quit()

if __name__ == "__main__":
    faceRecognize()
    playVideo(vidSource)
