import pickle

rec = []


def write():
    f = open("deadlck.dat", 'wb+')
    while True:
        n = input("Enter name:")
        r = int(input("enter roll:"))
        data = [r, n]
        rec.append(data)
        choice = input("Do you wanna continue :(y/n):")
        if choice in "nN":
            break
    pickle.dump(rec, f)
    f.close()


def read():
    f = open("deadlck.dat", "rb")
    for i in pickle.load(f):
        print(i)
    f.close()


def update():
    fnd = 0
    f = open("deadlck.dat", 'rb+')
    rno = int(input("Enter the roll no. to be searched:"))
    for i in pickle.load(f):
        if i[0] == rno:
            i[1] = input("Enter the name to be updated:")
            fnd = 1
            break
    if fnd == 0:
        print("record doesn't exist ")

    f.close()


def search():
    fnd = 0
    f = open("deadlck.dat", "rb+")
    r = int(input("Enter the roll no. to be searched : "))
    for i in pickle.load(f):
        if i[0] == r:
            print(i)
            fnd = 1
            break
    if fnd == 0:
        print("record not found ")


update()
read()
