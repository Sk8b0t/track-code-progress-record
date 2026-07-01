import mysql.connector
con=mysql.connector.connect(host="localhost",
                            user="root",
                            password="6996",
                            database="fuku")
if con.is_connected():
    print("हो गया रे लाला ")


cur=con.cursor()
org=input("Enter Org name:")
cur.execute("select Name,Org,city from vct_2024 where Org='%s' and result='failed' " % (org))
data=cur.fetchall()
print(*data,sep="\n")

m=input("Enter marks")
res=input("Enter stream")
cur.execute("select * from stu where total_marks>{} and stream='{}'".format(m,res))
data1=cur.fetchall()
print(*data1,sep="\n")
print("देख ले sql में हुआ की नहीं!! ")
