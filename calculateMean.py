import csv

with open("projects/project-104/data.csv",newline="") as f:
        reader=csv.reader(f)
        file_data=list(reader)
file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    n_num=file_data[i][2]
    newdata.append(float(n_num))
totalNumber=len(newdata)
total=0
for x in newdata:
    total+=x
mean=total/totalNumber
print("mean : "+str(mean))
