'''
block to reuse
Functions:
2 types: 
 1) Predefined : print(),input(),len(),add(),append(), pop(),remove() ...
 2) User defined : We will develop
    a) PNRN - Passing Nothing Returns Nothing
    b) PSRN - Passing Something Returns Nothing
    c) PNRS - Passing Nothing Returns Something
    d) PSRS - Passing Something Returns Something
'''
'''
#1) PNRN - Passing Nothing Returns Nothing
def printName(): #funtion definition
   name = input("Enter name: ")
   print(name)

printName() #function calling
printName()

#2) PSRN - Passing Something Returns Nothing
def printName(na):
   print(na)

name = input("Enter name: ")
printName(name)

'''
'''
#3) PNRS - Passing Nothing Returns Something
def printName():
    name = input("Enter name: ")
    return name

#method
result = printName()
print(result)

print(printName())'''

'''
#4) PSRS - Passing Something Returns Something
def printName(name):
    print(id(name))
    return name

#method
name = input("Enter name: ")
result = printName(name)
print(result)


print(printName(name))
'''
'''
#function arguments
#default arguments
def value(a,b,c=0):
    print(a+b+c)

value(2,3,5)
value(4,7)
#only default arguments allowed after default 
'''
'''
#keywords arguments
def greet(d,name,age):
    print(f"Name: {name}, Age: {age}")

# greet("john",34)
# greet(45,"Sam")
greet(34,age=23,name="Sam")
#only keywords arguments allowed after keyword arguments 
'''

#Variable-length positional arguments (*args)
# to accept any numbers of positional arguments
'''
def add(*numbers):
    numbers = list(numbers)
    print(type(numbers))
    return sum(numbers)

print(add(1,2,3))
#print(add([34,2,6,8])) #error
print(add(2,6,7,5,4,8))
'''
'''
def add(*numbers):
    numbers = list(numbers)
    print(type(numbers))
    return numbers

print(add("hello",34.6,54,True))
'''

#Variable-length keyword arguments(**kwargs)
#used to accept any number of keyword arguments
'''
def display(**info):
    print(type(info))
    print(info)
    for key,value in info.items():
        print(f"{key}: {value}")
    
display(name="Alice",age=34)
display(name="Alice",age=34,city="New York")
'''
'''
#mixing different argument types
def example(a,b=10,*args,**kargs):
    print(a)
    print(a,b)
    print(args)
    print(kargs)

example(1,2,3,4,x=5,y=6)
'''

#def function_name(parameter) -> return_type:
   #code
'''
def add(a,b) -> int:
    return a+b
print(add(4,5))


def add(a,b) -> None:
    print(a+b)
print(add(4,5))
'''
'''
def add(a:int,b:int) -> int:
    return a+b
print(add(4,5))
'''
'''
def display_student(student:dict) -> None:
    print(student)

student = {
    "Name": "John",
    "age": 34
}
display_student(student)
'''
'''

def display_student(student:dict[str,int]) -> None:
    print(student)

student = {
    "marks": 45,
    "age": 34
}
display_student(student)
'''

'''
1) 
'''
#help(list)
#print(dir(list))
print(help(list.reverse))

'''
Smart Student Management System

Build a menu-driven Student Management System using Python functions.

The project should use all major function concepts:

Positional arguments
Keyword arguments
Default arguments
*args
**kwargs
Type hints
Return values
Functions with no arguments
Functions with arguments
Functions returning multiple values
Functions calling other functions

Project Requirements

Your program should have this menu:

===== STUDENT MANAGEMENT SYSTEM =====


1. Add Student
2. Display Students
3. Search Student
4. Calculate Student Result
5. Update Student
6. Delete Student
7. Generate Class Report
8. Exit


Store students in a dictionary like:

students = {
    101: {
        "name": "Rahul",
        "age": 20,
        "course": "Python",
        "marks": [85, 90, 78]
    }
}
'''










