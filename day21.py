#continue file handling
import json
import csv
# f = open ('data.csv')
# print(f.read())
# f.close()


with open ('data.csv')as f:
    data = csv.reader(f)
    print(data)
    for i in data:
        print(i)


upload = [["3","Hari","dang"],["4","sita","Ktm"]]
with open ('data.csv','a', newline="") as f:
    data = csv.writer (f)
    data.writerows(upload)


with open ('data.json') as f:
    data = json.load(f)
    print(data)


data = {"name":"Rajat", "age": 25}
with open ("data.json","w") as file:
    json.dump(data,file, indent = 4)