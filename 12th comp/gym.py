import mysql.connector as a

con = a.connect(host="localhost", user="root", passwd="6996",database="gym")
cur = con.cursor()


def createDatabase():
    cur.execute("create database gym")
    con.commit()


def createTable():
    cur.execute(
        "create table January(Sno int primary key,name varchar(69) not null,arrival datetime , departure datetime,payment varchar(69) default 'unpaid')")


def inputValues():
    while True:
        n = input("Enter client name:")
        arr = input("Enter time of arrival(YYYY-MM-DD HH:MI:SS): ")
        dep = input("Enter time of departure: ")
        pay = input("Enter 'paid' if payment complete")
        cur.execute("inset into gym values('{}','{}','{}',{})".format(n, arr, dep, pay))
        ch = input("do you wanna continue?(Y/N)")
        if ch in "Nn":
            break
    con.commit()


def display():
    cur.execute("select * from gym ")
    print(*cur.fetchall(), sep="\n")



inputValues()
display()