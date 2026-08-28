#Ternary Operator - is a short way to write  if-else codition in one line
'''
age = int(input("Enter age: "))
result = "Adult" if age>18 else "Minor"
print(result)

marks = int(input("Enter marks: "))
grade = "A" if marks>=80 else "B" if marks>=60 else "C"
print(grade)'''

'''
#NUMBER GUESSIG GAME
import random
secret_number = random.randint(1,10)
print("Guess a number between 1 and 10: ")
print("You have 3 attempts")
for attempt in range(1,4):
    guess = int(input(f" Attemps: {attempt}: Enter your guess: "))
    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Congratulations! You guessed it!")
        break
else:
    print("You used all 3 attempts!")
    print("The correct number was: ",secret_number)
'''
'''
#continue -> skip the current iteration
even_count = 0
odd_count = 0
for i in range(1,11):
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative Number Skipped")
        continue
    if num%2 == 0:
        even_count +=1
    else:
        odd_count +=1
print("Even number: ",even_count)
print("Odd number: ",odd_count)
'''
'''
for i in range(1,11):
    pass

print("Hello")
'''
'''
marks = 85
match marks:
    case x if x>=90:
        print("Excellent")
    case x if x>=75:
        print("Very Good")
    case x if x>=50:
        print("Good")
    case _:
        print("Fail")
'''

'''LIST IN PYTHON 
Ordered
Mutable(can be changed)
Can contain different data types
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











