
import mysql.connector,openpyxl
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="School"
)
cursor=conn.cursor()
wb_obj=openpyxl.load_workbook("School.xlsx")
sheet=wb_obj.active

query="""INSERT INTO SchoolTb (name, Roll_no, class, percentage, contact) VALUES (%s,%s,%s,%s,%s)"""
for r in range(2,sheet.max_row):
    name    =sheet.cell(r,1).value
    roll =sheet.cell(r,2).value
    Class =sheet.cell(r,3).value
    percentage=sheet.cell(r,4).value
    contact =sheet.cell(r,5).value
    
    values=(name,roll,Class,percentage,contact)
    cursor.execute(query,values)
cursor.close()
conn.commit()
conn.close()
print(cursor.rowcount, "was inserted.")