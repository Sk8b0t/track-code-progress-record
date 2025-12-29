import csv

rec = []


def write():
    f = open("aur.csv", "w+", newline="")
    likho = csv.writer(f)
    likho.writerow(["roll", "name"])
    while True:
        n = input("Enter name:")
        r = int(input("enter roll:"))
        data = [r, n]
        rec.append(data)
        choice = input("Do you wanna continue :(y/n):")
        if choice in "nN":
            break
    likho.writerows(rec)
    f.close()


def read():
    f = open("aur.csv", 'r')
    padho = csv.reader(f)
    for i in padho:
        print(i)

read()
