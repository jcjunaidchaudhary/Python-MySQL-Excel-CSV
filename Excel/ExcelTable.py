import mysql.connector
database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="School"
)

mycursor=database.cursor()

#mycursor.execute("CREATE TABLE ExcelTable(name VARCHAR(20),roll_no int not null,class VARCHAR(5),percentage decimal(5,4),contact VARCHAR(10))")
#mycursor.execute("alter table ExcelTable add roll_no int AFTER name")
#mycursor.execute("ALTER TABLE ExcelTable DROP roll_no")
#mycursor.execute("DELETE FROM ExcelTable WHERE name='umar'")

qury="INSERT INTO ExcelTable (name,class,contact) VALUES (%s,%s,%s)"
val=("umar","V","9876543")
mycursor.execute(qury,val)

database.commit()