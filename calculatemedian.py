import csv
with open("projects/project-104/data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    newdata.append(float(n_num))
totalNumber=len(newdata)
newdata.sort()
if (totalNumber%2==0):
    median1=float(newdata[totalNumber//2])
    median2=float(newdata[totalNumber//2 - 1])
    median=(median1+median2)/2
else:
    median=newdata[totalNumber//2]

print("median : "+ str(median))