'''
modules: .py -> function, list, tuple, dict, set, class, objects, file hndlig,  
TWO TYPES:
  1) PREDEFINED -> already developed
    import random

     pip3 install pandas
     import pandas

import random
  2) USER DEFINED
'''
'''
#1)  PREDEFINED MODULES
import math
print(math.pi,math.e)
print(math.sqrt(25))
print(math.pow(2,3))
print(math.factorial(5)) #5-> 1x2x3x4x5
print(math.ceil(4.2),math.ceil(4.9))
print(math.floor(4.2),math.floor(4.9))
print(math.fabs(-10))
print(math.gcd(12,8))
print(math.lcm(4,8))
print(math.log(10))
print(math.isqrt(25))
print(math.isqrt(26)) #5.099

#help(math)
'''
'''
#random
import random as r
print(r.random()) #0-1
print(r.random() * 10) # 1-10
print(r.uniform(10,20))
print(r.randint(1,20))

if r.random() < 0.30:
    print("Event happened")
else:
    print("Event did not happen")


numbers= [1,2,3,4,5,6,7,8]
r.shuffle(numbers)
print(numbers)
#r.seed(23)
r.shuffle(numbers)
print(numbers)
r.shuffle(numbers)
print(numbers)

fruits = ['Apple','Banana','Kiwi','Orange']
x = r.choice(fruits)
print(x)
'''

import calendar as c
print(c.calendar(2026))
print(c.month(2026,6))
print(c.monthrange(2026,4))

for month in range(1,13):
    print(month,c.month_name[month])

for day in c.day_name:
    print(day)




#year, month, day - find weekday when person born - use weekday()
# number of day in a all month - use monthrange(year,month)







