'''
RELATIONAL/COMPARISION(>,<,>=,<=,==,!=) -> always returns True or False
'''
'''
print(5>2)
print(3<2)
print(3>=2)
print(6<=6)
print(2==8)
print(3!=3)
print(2!=4)
'''

#=(assignment) and ==(comparision)

'''
LOGICAL  OPERTORS(and or not)
'''
'''
#and -> If both conditions are True then only returns True otherwise False
print(3>2 and 2>1)
print(3>2 and 2<1)
print(3<2 and 2>1)
print(3<2 and 2<1)

#or -> If both conditions are False then only returns False otherwise False
print(3>2 or 2>1) 
print(3>2 or 2<1)
print(3<2 or 2>1)
print(3<2 or 2<1)
'''
'''
#not-> True-> False , False-> True
print(not(True))
print(not(False))
print(not(2)) #apart from 0 everything in python is True
print(not(0))
print(not(-3))
print(not(7>3))
print(not(5>2 and 7<1))
print(not('Hello')) #apart from empty sting everything is True
print(not(' '))
print(not(''))
'''

'''
#4) MEMBERSHIP OPERATOR(in, not in) -> only works with sequences
print('h' in 'hello')
print('H' in 'hello')
#print(3 in 2345) #ERROR
print(3 in [2,3,4,56])
print(4 in (2,5,7,8))
print('h' not in 'hello')'''

'''
#5) IDENTITY OPERATOR(is, is not) -> compare object location
x = 2
y = 2
print(x == y) #compare values
print(x is y) #compares object location
print(id(x),id(y))
y = 2.0
print(x == y)
print(x is y)
print(id(x),id(y))
print(x is not y)
'''
'''
x = 3
y = 2
print(id(x),id(y))
y = x
print(id(x),id(y))
'''
'''
#BITWISE OPERATOR(&(and),|(or),^(XOR/Exclusive OR),~(not),>>(right shift),<<(left shift))
print(6&5)
print(6|5)
print(6^5)
print(~(3)) #add 1 and then add negtive/ 1's and 2's complement
print(~(6))'''

num = 23
print(bin(num))








