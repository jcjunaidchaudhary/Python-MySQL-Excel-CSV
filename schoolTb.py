import mysql.connector,functools

myconec=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="School"
)

cur=myconec.cursor()

#cur.execute("CREATE TABLE SchoolTb(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20),class VARCHAR(5),percentage decimal(5,4),contact VARCHAR(10))")
#cur.execute("ALTER TABLE SchoolTb add Roll_no int(10) AFTER name")
# cur.execute("ALTER TABLE SchoolTb MODIFY percentage float")
#cur.execute("select* from SchoolTb")
#cur.execute("ALTER TABLE SchoolTb DROP COLUMN id")
# cur.execute("DELETE t1 FROM SchoolTb t1 INNER JOIN SchoolTb t2 WHERE t1.Roll_no>=t2.Roll_no")
# cur.execute("ALTER TABLE SchoolTb MODIFY Roll_no int PRIMARY KEY")
cur.execute("select Roll_no from SchoolTb")
myresult=cur.fetchall()
print("Total number of rows in table: ", cur.rowcount)
# lst=list(myresult)
print("\nPrinting each row")
for x in myresult:
    res=functools.reduce(lambda sub:sub*10,x)
    print(res)

print(myresult)

myconec.close()