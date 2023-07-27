import xlrd
import MySQLdb

# Open the workbook and define the worksheet
book = xlrd.open_workbook("D:\jc_junaid_chaudhary\MysqlPractice\Excel\School.xls")
sheet = book.sheet_by_name("source")

# Establish a MySQL connectiondatabase = MySQLdb.connect (host="localhost", user = "root", passwd = "", db = "mysqlPython")
conn=MySQLdb.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="School"
)
# Get the cursor, which is used to traverse the database, line by line
cursor = conn.cursor()

query="""INSERT IGNORE INTO SchoolTb (name, Roll_no, class, percentage, contact) VALUES (%s,%s,%s,%s,%s)"""
for r in range(1,sheet.nrows):
    name    =sheet.cell(r,1).value
    Class =sheet.cell(r,3).value
    percentage=sheet.cell(r,4).value
    contact =sheet.cell(r,5).value
    roll =sheet.cell(r,2).value
    
    values=(name,roll,Class,percentage,contact)
    cursor.execute(query,values)
cursor.close()
conn.commit()
conn.close()
print(cursor.rowcount, "was inserted.")