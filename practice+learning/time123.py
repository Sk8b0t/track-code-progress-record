import time
def pr(l):
    print("loading", end="")
    for i in range(6):
        print("..", end="")
        time.sleep(1)
    print("\n", time.asctime(time.localtime(time.time())))


    for i , item in enumerate(l):
     print(f"Theelement at {i}th index is {item}")
if __name__ == '__main__':
    l = ["sayan", "nayas", "njr", "NeymarJr"]
    pr(l)