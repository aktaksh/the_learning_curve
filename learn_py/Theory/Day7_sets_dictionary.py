
1) unordered
2) unique, no duplicacy
3) Mutable (changeable)


s = {} #empty dictionary
print(type(s))

s = set()
print(type(s))

s = {"Hello",34,1287.5,True,34,11,76,99,90,43}
print(type(s))
print(s)

#ADDING ELEMENTS
s.add(False)
print(s)

#ADDING MULTIPLE ITEMS
s.update(["John",87])
print(s)

#REMOVING
s.remove("John")
print(s)
# s.remove("John")#error if data not available

s.discard("John")
print(s)

#UNION -> ALL
a = {1,2,3,4}
b = {3,4,5,6}
print(a|b)
print(a.union(b))

#INTERSECTION - COMMON
print(a&b)
print(a.intersection(b))

#difference
a = {4,2,8,1}
b = {2,4,9,3}
print(a-b)

#symmetric difference - NO COMMON
print(a ^ b)

print(len(s))
for i in s:
    print(i)
    

#dictionary -------------------------------------

key-value
changeable
to get value you need key
No indexing


d = {}
print(type(d))

students = {
    "John": 86,
    "Harry":76,
    "Sam":45
}
print(students)

#ACCESSING VALUES
print(students["John"]) #error if not exists
print(students.get("Harry")) #no error if no exists

#ADDING NEW ITEM
students["Xavier"] = 67
print(students)

#UPDATE
students["Xavier"] = 89
print(students)

#REMOVING ITEM 
students.pop("John")
print(students)

del students["Harry"]
print(students)

del students
#print(students)

students = {
    "John": 86,
    "Harry":76,
    "Sam":45
}

print(students.keys())
print(students.values())
print(students.items())

for name,marks in students.items():
    print(name,marks)

print(len(students))

#NESTED DICTIONARY
students = {
    "student1":{
        "name":"John",
        "marks":45
    },
    "student2":{
        "name":"Sam",
        "marks":34
    }
}
print(students["student2"]["name"])

students.clear()
print(students)

