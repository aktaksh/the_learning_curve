
POLYMORPHISM: One Interface many forms
the same method/operator can behave differently depending on the 
object or data it is working with


print(10+20) #addition
print("Hello " + "John") #concatenation


#1) Method overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog()
cat = Cat()
dog.sound()
cat.sound()


#METHOD OVERRIDING
class Shape:
    
    def calculate_area(self):
        print ("CALCULATE AREA.")
        
class Circle(Shape):
    def __init__(self,Radius):
       self.Radius = Radius
    
    def calculate_area(self):
        CircleArea = 3.14*self.Radius*self.Radius
        print (f"The area of circle is {CircleArea}")

class Rectangle(Shape):
    def __init__ (self, Length , Width):
        self.Length = Length
        self.Width = Width

    def Calculate_area(self):
        RectangleArea= self.Length * self.Width
        print(f"The area of Rectangle is {RectangleArea} ")

C = Circle(7)
R = Rectangle(10, 5)
C.calculate_area()
R.Calculate_area()


#ABSTRACTION 
means hiding the internal implementation details and showing only 
essential functionality to the user

We can not create object of abstract class
note: If abstract class is being inherited in child, all the abstract 
methods of parent class should be defined in the child class
Abstract methods are used when you want to force all child classes to follow the same interface.

from abc import ABC, abstractmethod #ABC-> ABSTRACT BASE CLASS
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")
    def sound2(self):
        print("Cat Meows 2")

#ani = Animal() #error
dog = Dog()
dog.sound()

cat = Cat()
cat.sound()
cat.sound2()








