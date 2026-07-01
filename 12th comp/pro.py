# rollnol,name stream,
import mysql.connector as a

con = a.connect(host="localhost", user="root", password="6996", database="demo")
cur = con.cursor()


def create_table():
    cur.execute(
        "create table demon(rollno int primary key,name varchar(69) not null,stream varchar(69) not null,gender varchar(2) default 'F')")


def enter_values():
    while True:
        r = int(input("Enter roll no."))
        n = input("Enter name")
        s = input("Enter stream")
        cur.execute("insert into demon(rollno,name,stream) values({},'{}','{}')".format(r, n, s))
        ch = input("Do you wanna enter more(y/n)")
        if ch in "nN":
            break
    con.commit()


def search():
 while True:
    count=0
    print("press 1 for searching records with roll no.")
    print("press 2 for searching records with stream")
    print("press 3 for searching records with name")
    ch = int(input("Enter your choice: "))

    if ch == 1:
        roll = input("Enter the roll no. to be searched: ")
        cur.execute("select * from demon where rollno={}".format(roll))

    if ch == 2:
        stream = input("Enter the stream to be searched: ")
        cur.execute("select * from demon where stream='{}'".format(stream))
    if ch == 3:
        name = input("Enter the name to be searched: ")
        cur.execute("select * from demon where name='{}'".format(name))
    for i in cur.fetchall():
        count=1
        print(i)
    if count!=1:
         print("No such recorexists")
    inp=input("do you wanna search more??(y/n)")
    if inp in "nN":
       break


def show():
    cur.execute("Select * from demon")
    print(*cur.fetchall(), sep="\n")


search()
