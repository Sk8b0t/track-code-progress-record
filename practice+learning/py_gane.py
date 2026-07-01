from pygame import mixer
from datetime import datetime as d
from time import time


def ringAlarm(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break


def storeLog(msg):
    with open("logfile.txt", "a") as f:
        f.write(f"{msg}: {d.now()}\n")


def reminder(initialWaterTime, initialExerciseTime):
    rw = 5
    re = 12
    while True:
        if time() - initialWaterTime > rw:
            print("Reminder: Drink Water")
            ringAlarm("a.mp3", "s")
            storeLog(f"Reminder: Drink Water ->{d.now()}")
            initialWaterTime = time()

        elif time() - initialExerciseTime > re:
            print("Reminder: do exercise")
            ringAlarm("a.mp3", "s")
            storeLog(f"Reminder: do exercise  ->{d.now()}")
            initialExerciseTime = time()


if __name__ == '__main__':
    water = time()
    ex = time()
    reminder(water, ex)
