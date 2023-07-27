import csv

with open('myfile.csv','r',newline='') as csvfile:
    readit = csv.reader(csvfile,delimiter=',')
    red=list(readit)
    for line in red:
        print(line)
    # writeit=csv.writer(csvfile,delimiter=',')
    # writeit.writerow(['Hashim','Bcom',98765432])

# file=open('myfile.csv','a',newline="")
# writeit=csv.writer(file,delimiter=',')
# writeit.writerow(['hashim',12,'VI'])   
# file.close()