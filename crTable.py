import mysql.connector

myconn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="world"
)

cur=myconn.cursor()

try:
    dbs=cur.execute("create table Employee(name varchar(20) not null,id int(20) not null primary key,salary float not null,Dept_id int not null)")
except:
    myconn.rollback()
myconn.close()