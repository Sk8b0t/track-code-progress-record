import csv


def write():
    f = open("sayan1.csv", "w+", newline="")
    likho = csv.writer(f)
    likho.writerow(["rollNo", "name", "marks"])
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
    likho.writerows(record)
    f.close()


def read():
    f = open("sayan1.csv", "r")
    padho=csv.reader(f)
    for i in padho:
        print(i)
    f.close()


read()