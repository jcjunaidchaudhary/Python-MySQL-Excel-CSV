import openpyxl

wb_obj=openpyxl.load_workbook("School3.xlsx")
sheet_obj=wb_obj.active

line=0
row_value=[]
for row in sheet_obj.values:
    line += 1
    if line==1:
        continue
    else:
        print(row[1])
        row_value.append(row)