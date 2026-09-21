'''
OOP: Object Orinted Programming
class: Binding Data(fields/Variables) and behaviors(methods/functions) -> Encapsulation
object: instance of class
OOPS 4 PIILORS: Encapsulation, Inheritance, Polymorphism, Abstraction

Initializer/Constructor : Initializes object values
                          First parameter will store object reference only
                          initializer gets called automtically while creation of the object
'''
'''
class Student_classroom:
    def __init__(self,name,roll): #self->stored  object reference
                                #__init__ is a i initializer 
       # print(self)
       self.name = name
       self.roll = roll

    def greet(self):
        print(f"My name is {self.name}, My roll number is {self.roll}")


s1 = Student_classroom("John",101)
s2 = Student_classroom("Harry",102)
s3 = Student_classroom("Peter",104)
s1.greet()
s2.greet()
s3.greet()
'''

'''
class Student_classroom:
    def __init__(self,name,roll): #self->stored  object reference
                                #__init__ is a i initializer 
       # print(self)
       self.name = name
       self.roll = roll

    def greet(self):
        print(f"My name is {self.name}, My roll number is {self.roll}")

students = [
Student_classroom("John",101),
Student_classroom("Harry",102),
Student_classroom("Peter",104)
]

for student in students:
    student.greet()
'''


class Student_classroom:
    def __init__(self,name,roll): #self->stored  object reference
                                #__init__ is a i initializer 
       # print(self)
       self.name = name
       self.roll = roll

    def greet(self):
        print(f"My name is {self.name}, My roll number is {self.roll}")

students = [] #list of objects
n = int(input("How many Students? "))
for i in range(n):
    name = input("Enter name: ")
    roll = int(input("Enter rollno: "))

    student = Student_classroom(name,roll)
    students.append(student)


for student in students:
    student.greet()