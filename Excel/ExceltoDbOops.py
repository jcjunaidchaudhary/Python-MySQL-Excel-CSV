import mysql.connector,openpyxl

dbc =("localhost","root","root","school")
table="SchoolTb"
class sql:
    db = mysql.connector.connect(dbc[0],dbc[1],dbc[2],dbc[3])
    cursor = db.cursor()
    cursor.execute("select Roll_no from SchoolTb")
    myresult=cursor.fetchall()
    existing=[]
    for x in myresult:
        lst=list(x)
        existing+=lst
    row=0

    def __init__(self,file):
        wb_obj=openpyxl.load_workbook(file)
        sheet=wb_obj.active

        updatequery=f"""update {{table}}  
        set name=%s, class=%s, percentage=%s, contact=%s
        where Roll_no=%s"""
        insertquery=f"""INSERT INTO {{table}} (name, Roll_no, class, percentage, contact) 
                VALUES (%s,%s,%s,%s,%s)"""

        #code
        for r in range(2,sheet.max_row+1):
            self.name    =sheet.cell(r,1).value
            self.roll =sheet.cell(r,2).value
            self.Class =sheet.cell(r,3).value
            self.percentage=sheet.cell(r,4).value
            self.contact =sheet.cell(r,5).value
            
            insertvalues=(self.name,self.roll,self.Class,self.percentage,self.contact)
            updatevalues=(self.name,self.Class,self.percentage,self.contact,self.roll)

            if self.roll in sql.existing:
                sql.cursor.execute(updatequery,updatevalues)
                sql.row+=sql.cursor.rowcount     
            else:        
                sql.cursor.execute(insertquery,insertvalues)
                sql.row+=sql.cursor.rowcount
    
    def __str__(self) -> str:
        return f"{self.row} was inserted."

    cursor.close()
    db.commit()
    db.close()

db=sql("SchoolClass.xlsx")
