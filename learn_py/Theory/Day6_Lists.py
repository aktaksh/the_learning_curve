
'''LIST IN PYTHON 
Ordered
Mutable(can be changed)
Can contain different data types
'''
'''
number = [] #empty list
print(type(number))

number = list() #empty list
print(type(number))

l1 = ["Hello",34,34.7,True]
print(l1)

for i in l1:
    print(i)

#ACCESSING ELEMENTS
print(l1[0],l1[2],l1[-1])

#MUTABLE
l1[0] = "John"
print(l1)

#ADDING ELEMENT
l1.append(78) #add data at last
print(l1)

#AT specific location
l1.insert(2,"Harry")
print(l1)

#REMOVING ELEMENTS
l1.remove(78)
print(l1)
#l1.remove(78) #if value not available then remove


l1.pop() #removes last element
print(l1)

#INDEXING
print(l1.index("John"))
print(len(l1))

# take a list of fruits and search a specific fruits
# find the sum of all numbers in a list
# remove duplicates values from a list
# replace every negative number in a list with 0
# move all zeros to the end of the list.
# find common elements between 2 lists
# reverse a list using loop
'''
'''
#SLICING IN LIST - start stop(excluded) step
numbers = [10,20,30,40,"Hello",True]
print(numbers[1:4])
print(numbers[:3])
print(numbers[3:])
print(numbers[:])
print(numbers[::2])
print(numbers[::-1])
'''
'''
#tuple -> immutable(no change)
t = () #tuple
print(type(t))

t = (45) #int 
print(type(t))

t = (45,)
print(type(t))

t = 45,
print(type(t))

#ACCESSING ELEMENTS
t = ("Hello",True,76,34.5,10,10,10)
print(t[0])
print(t[-1])
print(t[1:3])

#IMMUTABLE
#t[0] = "John" #error
print(t)
print(t.count(10))
print(t.index("Hello"))


student = ("John",32,87) #packing
name,age,marks = student #unapacking
print(name,age,marks)

print(len(student))
numbers = (12,43,11,65,87,11,45)
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(sorted(numbers))

numbers = [10,20,30,40,50]
result = tuple(numbers)
print(result)

#reverse()
numbers = (12,43,11,65,87,11,45)
result = reversed(numbers)
print(tuple(result))
'''


#dunder method - double underscore
'''
Special methods whose names start and end with __ underscore
'''
'''
# __init__() -> CONSTRUCTOR/INITIALIZER - runs automatically when an object is created
class Student:
    def __init__(self,name,age):
        print(self)


s1 = Student("John",23,78)
s2 = Student("Harry",23,56)
'''

if __name__ == "__main__":
    print("Program Started")

