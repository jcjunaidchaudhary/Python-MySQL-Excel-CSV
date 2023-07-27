import mysql.connector,openpyxl
import csv

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="apitest"
)
cursor=conn.cursor()
insertquery="""INSERT INTO Student (name, std, course) 
            VALUES (%s,%s,%s)"""
 
with open('myfile.csv') as file:
    readit=csv.reader(file)
    i=0
    for row in readit:
        i+=1
        # title,desc,author=row
        if i==1:
            continue
        else:
            cursor.execute(insertquery,row)

cursor.close()
conn.commit()
conn.close()