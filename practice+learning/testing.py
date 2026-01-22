from pygame import mixer
from datetime import datetime as d
from time import time,sleep
def playMusic(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def reminder():
    r=10

if __name__ == '__main__':



