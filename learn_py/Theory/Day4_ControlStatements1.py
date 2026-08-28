'''
CONTROL STATMENTS:
  1) CONDITIONAL: if-else, elif, nested if, match, ternary
  2) LOOPING: for, while, for-else, while-else
  3) JUMPING: break, continue, pass
'''
'''
if 5<2:
    print("hello")
else:
    print("Hi")

balance = 1000
amount = int(input("Enter Withdrawl amount: "))
if amount <= balance:
    balance -= amount
    print("WITHDRAWL SUCCESSFUL")
    print("REMAINING BALANCE: ",balance)
else:
    print("INSUFFICIENT BALANCE")
    '''
'''
#elif else
units = int(input("Enter Units: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10
print("ELECTRICITY BILL: ", bill)
'''
'''
#nested if
username = input("Enter Username: ")
if username == "admin":
    password = input("Enter Password: ")
    if password == "admin123":
        print("LOGIN SUCCESSFUL!")
    else:
        print("INCORRECT PASSWORD!")
else:
    print("INCORRECT USERNAME!")
'''
'''
Mini Project: ATM Banking System
Scenario

Create a simple ATM program where the user enters their PIN. If the PIN is correct, show an ATM menu:

1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit

The program should perform different operations based on the user's choice.

Rules
Allow 3 PIN attempts.
If the PIN is correct, show the menu.
For withdrawal:
Amount must be greater than 0.
Amount must be a multiple of 500.
Amount must not exceed the account balance.
For deposit:
Amount must be greater than 0.
Display the updated balance after a successful transaction.
'''


