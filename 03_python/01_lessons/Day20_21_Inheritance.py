
#INHRITANCE: Allows one class(child/derived/sub) to acquire properties and methods of
another class(parent/base/super)
TYPES:
 1) Single
 2) Multiple
 3) Multilevel
 4) Hierarchical
 5) Hybrid -> Mix Inheitance


#1) Single -> One Parent -> One Child

class Animal:
    def eat(self):
        print("Animal eats!")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.bark()
d.eat()


class Animal:
    def __init__(self,name):
        self.name = name

    def display_animal(self):
        print("Animal name: ",self.name)

class Dog(Animal):
    def __init__(self,name,breed):
        #super().__init__(name)
        Animal.__init__(self,name)
        self.breed = breed

    def display_dog(self):
        print("Breed: ",self.breed)

dog1 = Dog("Tommy","Labrador")
dog1.display_animal()
dog1.display_dog()


#2) Multiple Inheritance - multiple parents single child


#2) Multiple - multiple parent one child
class Father:
    def gardening(self):
        print("Father knows gardening")

class Mother:
    def cooking(self):
        print("Mother knows cooking")

class Child(Father,Mother):
    def playing(self):
        print("Child lies playing")

c = Child()
c.gardening()
c.cooking()
c.playing()


class Father:
    def __init__(self,father_name):
        self.father_name = father_name

class Mother:
    def __init__(self,mother_name):
        self.mother_name = mother_name

class Child(Father,Mother):
    def __init__(self,father_name,mother_name,child_name):
       Father.__init__(self,father_name)
       Mother.__init__(self,mother_name)
       self.child_name = child_name

    def display(self):
        print(f"Father: {self.father_name}, Mother: {self.mother_name}, Child: {self.child_name}")


c = Child("David","Grace","Sam")
c.display()
print(Child.mro())

#MRO->  METHOD RESOLUTION ORDER


#3) Multilevel Inheritance -> Grandparents -> Parents -> Child

class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self,name,employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Manager(Employee):
    def __init__(self,name,employee_id,department):
        super().__init__(name,employee_id)
        self.department = department

    def display(self):
        print("Name: ",self.name)
        print("Employee ID: ",self.employee_id)
        print("Department: ",self.department)

m1 = Manager("Sam",101,"IT")
m1.display()


#4) Hierarchical Inheritance - One Parent Multiple Child
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Developer(Employee):
    def __init__(self,name,salary,langauge):
        super().__init__(name,salary)
        self.language = langauge

    def display(self):
        print("Developer: ",self.name)
        print("Salary: ",self.salary)
        print("Language: ",self.language)

class Manager(Employee):
    def __init__(self,name,salary,team_size):
            super().__init__(name,salary)
            self.team_size = team_size
    
    def display(self):
            print("Manager: ",self.name)
            print("Salary: ",self.salary)
            print("Team Size: ",self.team_size)

d1 = Developer("Harry",60000,"Python")
m1 = Manager("Peter",90000,10)
d1.display()
print()
m1.display()


#5)Hybrid Inheritance
class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person): 
    def __init__(self,name,employee_id):
        Person.__init__(self,name)
        self.employee_id = employee_id

class Student(Person):  #hierarcical
    def __init__(self, name,course):
        Person.__init__(self,name)
        self.course = course

class Intern(Employee,Student):  #multiple / multilevel
    def __init__(self, name, employee_id,course,duration):
        Employee.__init__(self,name, employee_id)
        Student.__init__(self,name,course)
        self.duration = duration

    def display(self):
        print("Name: ",self.name)
        print("Employee ID: ",self.employee_id)
        print("Course: ",self.course)
        print("Duration: ",self.duration)
        #print(f"Name: {self.name}, Employee ID: {self.employee_id}")

i1 = Intern("David",101,"Python","6 months")
i1.display()




