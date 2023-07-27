import mysql.connector

myconec=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

cur=myconec.cursor()

try:
    cur.execute("create database School")
    cur.execute("show databases")
except:
    myconec.rollback()

for x in cur:
    print(x)
myconec.close()