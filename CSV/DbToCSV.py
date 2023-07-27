from os import write
import mysql.connector
import csv

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='School'

)

cursor=conn.cursor()
cursor.execute("select* from SchoolTb")
result=cursor.fetchall()


file=open('Student.csv','w',newline="")
writeit=csv.writer(file,delimiter=',')
writeit.writerow(['Name','Roll No.','Class', 'Percentage','Contact'])
writeit.writerows(result)
file.close()
