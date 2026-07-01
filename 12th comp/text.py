import pickle


def write():
    f = open("sayan.dat", "wb+")
    record = []
    while True:
        name = input("Enter you name: ")
        stream = input("Enter you stream: ")
        marks = int(input("Enter you marks: "))
        data = [name, stream, marks]
        record.append(data)
        ch = input("Do you want to continue(Y/N)")
        if ch in "nN":
            break
    pickle.dump(record, f)
    f.close()


def append():
    f = open("sayan.dat", "ab+")
    record = []
    while True:
        name = input("Enter you name: ")
        stream = input("Enter you stream: ")
        marks = int(input("Enter you marks: "))
        data = [name, stream, marks]
        record.append(data)
        ch = input("Do you want to continue(Y/N)")
        if ch in "nN":
            break

    pickle.dump(record, f)


def read():
    f = open("sayan.dat", 'rb+')
    print(pickle.load(f))
    f.close()


def search():
    cnt = 0
    s = input("Enter your name: ")
    f = open("sayan.dat", 'rb+')
    data = pickle.load(f)
    for i in data:
        if i[0] == s:
            print("record found")
            print(i)
            cnt = 1
    if cnt!=1:
        print("record not associated with this name ")
    f.close()


read()
search()
