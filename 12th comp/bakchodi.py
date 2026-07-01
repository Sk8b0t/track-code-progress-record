import csv

rec=[]
def write():
    f = open("SK8BotOP.csv", "a", newline='')
    likho = csv.writer(f)
    #likho.writerow(['name', 'roll'])
    while True:
        n = input("Enter name:")
        r = int(input("Enter roll no."))
        likho.writerow([n,r])
        ch = input("Do u wanna continue:(Y/N)")
        if ch in "nN":
            break
    f.close()


def read():
    f = open("SK8BotOP.csv", "r")
    padho = csv.reader(f)
    for i in padho:
        print(i)
    f.close()


read()


