'''
JSON: JAVASCRIPT OBJECT NOTATION
Commonly used when working with APIs, Web application, Configuration files, Storing data
'''
import json
# python object  -> json data

'''
python   json
dict ->     object
list ->     array
str  ->     string
int, float -> number
True    -> true
False    -> false
None    -> null
'''
'''
#json.dumps() -> converts python obejct into json formatted string
student = {
    "name": "john",
    "age":23,
    "marks":86
}
print(type(student))
data = json.dumps(student)
print(data)
print(type(data))

#json.loads() -> means load from string
student = json.loads(data)
print(student)
print(type(student))

#dump -> converts into json file
#load -> loads from json file
'''
import csv
'''
with open("students.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(row)
'''
'''
with open("students.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print("Name: ",row[0])
        print("Marks:",type(row[2]))
        print("Marks:",int(row[2]))
        '''

#  #deletes all previous data
# with open("student1.csv",'w',newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["id","name","marks"])
#     writer.writerow([102,"Harry",34])


# with open("student1.csv",'a',newline="") as file:
#     writer = csv.writer(file)
#     #writer.writerow(["id","name","marks"])
#     writer.writerow([101,"John",34])
    


student = []
updated = False

with open("student1.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["name"] == "John":
            row["marks"] = "95"
            updated = True
        student.append(row)

with open("student1.csv",'w',newline="") as file:
    fieldnames = ["name","marks"]
    writer = csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(student)




