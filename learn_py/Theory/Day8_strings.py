'''identifiers
oerators
strings
list
tuple
sets
dictionaries
functions - pre, user, keywords, length variable, default
lambda
iterators
generators
decorators
exception handling
multithreading
file handling
OOPS - 4 pillars
numpy 
pandas
matplotlib
flask django
'''

#STRINGS
#String -> is a sequence of character enclosed in (',",''',""")
#String -> combination of characters

name = "Alice"
print(name)
name = 'John'
print(name)
message = "John's notebook"
print(message)
message = """welcome
            to
              python"""
print(message)

#ACCESSING CHARACTERS
text = "python"
print(text[0])
print(text[-1])

#SLICING start, stop(excluded), step
text = "Python"
print(text[0:3])
print(text[2:])
print(text[::-1])

#COMMON STRING OPERATIONS
a = "Hello"
b = "World"
print(a + " " + b) #concatention
print(a*3) #repetition
print(len(a))

#PRE DEFINED METHODS
text = "python programming"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
#print(text.replace("Python","Java")) #no change, need to check
print(text.split())
text = "py@thon prog@ramming"
print(text.split('@'))
text = "python programming"
print(text.find("pro"))
print("pro" in text)
print(text.count("p"))
text = "Python123"
print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.startswith("Py"))
print(text.endswith("he"))

#text[0] = "S" #error
#print(text)




name = "John"
age = 23
print(f"My name is {name} and I am {age}")



#help(str)
#python3 -c "help('modules')


#for loop
text = "python"
for i in text:
    print(i)

text = "python"
text = "E" + text[1:]
print(text)

text = "Python"
chars = list(text)
print(chars)
chars[0] = "M"
print(chars)
print(text)
text = "".join(chars)
print(text)
'''

 1) Find the number of occurrence of a word inside a sentence without substring.
 2) Password:
   At least 8 characters
   One uppercase letter
   one lowercase letter
   one digit
   one special character

3) Mask sensitive data
Given : 987676765487
output: ********3210

4) Caesar cipher
   Encrypt:
     HELLO
    by shifting every character by 3:
     KHOOR
'''

'''
Python, flask, django, GUI, ML, DS, NLP, GEN AI
C,C++,JAVA, REACT, ANGULAR,  MERN, MEAN,
SQL SERVER, MYSQL, MONGODB, ORACLE, ,net full stack, java full stack
web development , Azure ,Devops, Uipath, powerBI, Linux, Networking ...
'''






