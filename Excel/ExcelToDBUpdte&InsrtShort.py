import mysql.connector,openpyxl
from openpyxl.workbook import workbook

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="School"
)
cursor=conn.cursor()
wb_obj=openpyxl.load_workbook("School3.xlsx")
sheet=wb_obj.active

cursor.execute("select Roll_no from SchoolTb")
myresult=cursor.fetchall()
existing=[]
for x in myresult:
    lst=list(x)
    existing+=lst


updatequery="""update SchoolTb 
        set name=%s, class=%s, percentage=%s, contact=%s
        where Roll_no=%s"""
insertquery="""INSERT INTO SchoolTb (name, Roll_no, class, percentage, contact) 
        VALUES (%s,%s,%s,%s,%s)"""
                               

row=0

line=0
row_value=[]
for row in sheet.values:
    line += 1
    if line==1:
        continue
    else:
        print(row[1])
        row_value.append(row)


cursor.close()
conn.commit()
conn.close()
print(row, "was inserted.")