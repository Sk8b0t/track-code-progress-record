from pygame import mixer
from time import time
from datetime import datetime as d
def playMusic(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        if input()==stopper:
            break
def activityLog(msg):
    with open("logfile.txt","a")as f:
        f.write(f"{msg} -->{d.now()}")
def reminder(initialWaterTime,initialExerciseTime):
    r=5
    r1=10
    while True:
        if time()-initialWaterTime>r:
            a="Reminder: Drink water"
            playMusic("a.mp3","s")
            activityLog(a)
            initialWaterTime=time()
        elif time()-initialExerciseTime>r1:
            a="Reminder: DO exercise"
            playMusic("a.mp3",'s')
            activityLog(a)
            initialExerciseTime=time()
if __name__ == '__main__':
    water=time()
    ex=time()
    reminder(water,ex)



