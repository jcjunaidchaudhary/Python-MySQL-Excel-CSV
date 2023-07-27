
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
print("existing", existing)

# row=0
dic_data=[]

def addingDB(param): 
    print("param", param)
    queryInsert(param[1],param)
    row_value.clear()

def queryInsert(roll_no,values):
    row=0
    updatequery="""update SchoolTb 
        set name=%s, class=%s, percentage=%s, contact=%s
        where Roll_no=%s"""
    insertquery="""INSERT INTO SchoolTb (name, Roll_no, class, percentage, contact) 
            VALUES (%s,%s,%s,%s,%s)"""
    if roll_no in existing:
        cursor.execute(updatequery,values)
        row+=cursor.rowcount     
    else:        
        cursor.execute(insertquery,values)
        row+=cursor.rowcount
    
line=0
row_value=[]
for row in sheet.values:
    line += 1
    for value in row:
       if line==1:
           continue
       else:
           row_value.append(value)
    if line != 1:
        addingDB(row_value)



cursor.close()
conn.commit()
conn.close()
print(row, "was inserted.")
