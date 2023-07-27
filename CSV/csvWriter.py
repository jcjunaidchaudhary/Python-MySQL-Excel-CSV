import csv

file=open("School2.csv","w",newline='')

csv_writer=csv.writer(file,delimiter=',')

# csv_writer.writerow(['Name','Rollno.','class'])
csv_writer.writerow(['Asif','VII',1234567])


# csv_writer.writerows([['Junaid',12,'X'],['Umar',13,'XI']])

file.close()

# with open('myfile.csv','w') as f:
#     csv_writer=csv.writer(f,delimiter=',')
#     csv_writer.writerow(['Khalid',22,'V'])