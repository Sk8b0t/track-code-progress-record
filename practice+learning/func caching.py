import time
from functools import lru_cache
@lru_cache(maxsize=22)
def timeWaste(n):
    time.sleep(n)
    return n
if __name__ == '__main__':
    try:
        with open("wtf.txt","r") as f:
            print("Hey!")
            timeWaste(3)
            print("Now")
            timeWaste(4)
            print("calling...")
            timeWaste(3)
            print("yo wassup")
    except Exception as e:
        print(e)
    else:
        print("This will only run if except block isn't running")
    finally:
        timeWaste(3)
        print("This block will be executed anyways whether it is in try or except block")
    timeWaste(3)
    print("tmkc 10 bar")

