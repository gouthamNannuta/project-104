import csv
from collections import Counter
with open("projects/project-104/data.csv",newline="") as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
newdata=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    newdata.append(float(n_num))
totalNumber=len(newdata)
data=Counter(newdata)
modedataforrange={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for height,occurence in data.items():
    if(50 < float(height) < 60):
        modedataforrange["50-60"] +=occurence
    elif(60< float(height) < 70):
        modedataforrange["60-70"] +=occurence
    elif(70< float(height) < 80):
        modedataforrange["70-80"] +=occurence
moderange,modeoccurence=0,0
for range,occurence in modedataforrange.items():
    if occurence>modeoccurence:
        moderange,modeoccurence=[int(range.split("-")[0]), int(range.split("-")[1])],occurence
        
mode = float((moderange[0] + moderange[1]) / 2)
print(f"Mode is -> {mode:2f}")