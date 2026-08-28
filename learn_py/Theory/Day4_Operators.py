'''
#BITWISE OPERATORS 
print(25>>3) #towards right shift
print(25<<3)

#ASSIGNMENT OPERATOR(=,+=,-=,*=,/=,//=,%=,**=,&=,|=,~=,^=,>>=,<<=)
a = 7
a+=2
print(a)

b = 8
b+=4
print(b)

c = 9
c%=2
print(c)


c = 6
c &= 5
print(c)


Read = 1
Write = 2
Delete = 4
Admin = 8

READ  = 1<<0 #0001
WRITE = 1<<1 #0010
DELETE = 1<<2 #0100
ADMIN = 1<<3 #1000

print(READ,WRITE,DELETE,ADMIN)

user_permission = READ | WRITE
print(user_permission)

if user_permission & WRITE:
    print("USER CAN WRITE")
'''
'''
Create a Smart E-Commerce Checkout System in Python where the user enters product price, quantity, 
membership type, coupon code, and payment method. Calculate the subtotal,
 apply membership and coupon discounts, give an additional discount for bulk purchases, 
 calculate delivery charges based on the final amount, and validate the payment method. 
 Use appropriate arithmetic, comparison, logical, assignment, membership, identity, bitwise, and 
 conditional operators, along with if-elif-else and nested if-else, to determine the final payable
   amount and display a complete bill.
   '''

