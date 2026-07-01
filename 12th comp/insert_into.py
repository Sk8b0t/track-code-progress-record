import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="6996",database="fuku")
if con.is_connected():
    print("connected successfully")

cursor=con.cursor()
cursor.execute("alter table stu modify sno int default 0")

name=input("Enter name")
stream=input("Enter stream")
marks=input("Enter marks")
cursor.execute("insert into stu(name,stream,total_marks) values('{}','{}',{})".format(name,stream,marks))
data=cursor.fetchall()
print(*data,sep="")

cursor.execute("delete from stu where name='sayan'")
con.commit()
cursor.execute("select * from stu")
print(*cursor.fetchall(),sep="\n")
con.commit()
