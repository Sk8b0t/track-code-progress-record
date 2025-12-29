import mysql.connector as a
con=a.connect(host="localhost",
              user="root",
              passwd="12345",
              database="employee")
def npersonal():
    n=input("enter employee name ")
    c=input("enter employee city name  ")
    d=input("enter employee's D.O.B")
    p=input("enter employee Phone ")
    data =(n,c,d,p)
    sql='insert into personal values(%s,%s,%s,%s)'
    c=con.cursor()
    c.execute(sql,data)
    con.commit()
    print("Data Entered Successfully")
    main()

def personal():
    sql = "select * from personal"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()

def noffice():
    ec=input("Enter Employee code:")
    n=input("Enter Employee name:")
    ps=input("Enter Employee's post':")
    j=input("Enter Employee's joining date'")
    bp=input("Enter assigned salary:")
    data=(ec,n,ps,j,bp)
    sql = 'insert into office values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Entered Successfully")
    main()

def office():
    sql="select * from office"
    c=con.cursor()
    c.execute(sql)
    d=c.fetchall()
    for i in d:
        print(i)
    main()

def nsalary():
    ec=input("Enter Employee Code:")
    v=(ec,)
    sql="select BasicPay from office where Ecode=%s"
    c=con.cursor()
    c.execute(sql,v)
    bs=c.fetchone()
    n=input("Enter employee name:")
    y=input("Enter employee name:")
    m=input("Enter employee name:")
    wd=input("Enter employee name:")
    td  =input("Enter employee name:")
    fp=bs[0]/td*wd
    data=(ec,n,y,m,wd,fp)
    sql='insert into salary values(%s%s%s%s%s%s)'
    c=con.cursor()
    c.execute(sql,data)

def salary():
    sql = "select * from salary"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(i)
    main()

def main():
    print(""" 1. Add new employee personal details
    2.Display Employees Personal Details
    3.Add new employee office details
    4.display employee office details 
    5. enter salary details of employee
    6.display salary details of employee""")

    choice=input("enter task no.")
    while True:
        if (choice=="1"):
            npersonal()
        elif (choice == "2"):
            personal()
        elif (choice == "3"):
            noffice()
        elif (choice == "4"):
            office()
        elif (choice == "5"):
            nsalary()

        elif (choice == "6"):
            salary()
        else:
           print("wrong choice")
main()



