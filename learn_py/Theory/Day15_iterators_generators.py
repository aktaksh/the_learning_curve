'''
Iterator is an object that gives you one value at a time, and remembers
where it is in the sequences.
__iter__() -> returns the itertor itself

__next__() -> returns the next value
'''
'''
numbers = [10,20,30]
it = iter(numbers)
#print(list(it))

print(next(it))
print(next(it))

messages = ['login','payment','logout']
for message in messages:
    print(message)


it = iter(message)
first = next(it)
print("First: ",first)

#do some other work
print("check database...")

second = next(it)
print("Second: ",second)

#sending notification
print("sending notification...")

'''

'''
generator: is a simple way to create an iterator that produces values one at a time,
only when needed.
'''

def numbers():
    yield 10
    yield 20
    yield 30

gen = numbers()
print(next(gen)) 
# print(next(gen)) 
# print(next(gen)) 

#COMPREHENSIONS - CONCISE WAY TO CREATE COLLECTIONS FROM ANOTHER ITERABLE
numbers = []
for i in range(1,6):
    numbers.append(i*2)
print(numbers)

numbers = [i * 2 for i in range(1,6)] #list comprehension
print(numbers)

#with condition
even = [x for x in range(1,11) if x%2 == 0]
print(even)

#condition + transform
evenadd = [x*2 for x in range(1,11) if x%2 == 0]
print(evenadd)

#DICTIONARY COMPREHENSION
squares = {i:i*i for i in range(1,6)}
print(squares)

#SET COMPREHENSION
squares = {i*i for i in range(1,6)}
print(squares)

#lambda
'''
a small anonymous function - create without giving it a normal def name
'''
def add(a,b):
    return a+b

add = lambda a,b: a+b
print(add(2,4))

users = [
    {"name": "Alice","age":30},
    {"name": "Bob","age":20},
    {"name": "Charlie","age":25},
]

users.sort(key=lambda user: user["age"])
print(users)