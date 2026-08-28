syntax.cpp
if (condition) {
  // block of code to be executed if the condition is true
}
#include <iostream>
using namespace std;

int main() {
  cout << "Hello World!";
  return 0;
}
// This is a comment
cout << "Hello World!";

int - stores integers (whole numbers), without decimals, such as 123 or -123
double - stores floating point numbers, with decimals, such as 19.99 or -19.99
char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
string - stores text, such as "Hello World". String values are surrounded by double quotes
bool - stores values with two states: true or false


int x, y, z;
x = y = z = 50;
cout << x + y + z;

int x = 5, y = 6, z = 50;
cout << x + y + z;

float f1 = 35e3;
double d1 = 12E4;
cout << f1;
cout << d1;


bool isCodingFun = true;
bool isFishTasty = false;
cout << isCodingFun;  // Outputs 1 (true)
cout << isFishTasty;  // Outputs 0 (false)


char a = 65, b = 66, c = 67;
cout << a;
cout << b;
cout << c;


// Include the string library
#include <string>

// Create a string variable
string greeting = "Hello";

// Output string value
cout << greeting;

auto x = 5; // x is automatically treated as int


// Create variables of different data types
int items = 50;
double cost_per_item = 9.99;
double total_cost = items * cost_per_item;
char currency = '$';

// Print variables
cout << "Number of items: " << items << "\n";
cout << "Cost per item: " << cost_per_item << currency << "\n";
cout << "Total cost = " << total_cost << currency << "\n";


int sum1 = 100 + 50;        // 150 (100 + 50)
int sum2 = sum1 + 250;      // 400 (150 + 250)
int sum3 = sum2 + sum2;     // 800 (400 + 400)
/*

C++ divides the operators into the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Bitwise operators


Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3

Operator	Name	Description	Example	Try it
&& 	Logical and	Returns true if both statements are true	x < 5 &&  x < 10	
|| 	Logical or	Returns true if one of the statements is true	x < 5 || x < 4	
!	Logical not	Reverse the result, returns false if the result is true	!(x < 5 && x < 10)	


*/


int result1 = 2 + 3 * 4;     // 2 + 12 = 14
int result2 = (2 + 3) * 4;   // 5 * 4 = 20

cout << result1 << "\n";
cout << result2 << "\n";


string firstName = "John ";
string lastName = "Doe";
string fullName = firstName + lastName;
cout << fullName;


string firstName = "John";
string lastName = "Doe";
string fullName = firstName + " " + lastName;
cout << fullName;


if (20 > 18) {
  cout << "20 is greater than 18";
}

int time = 16;

if (time < 12) {
  cout << "Good morning.";
} else if (time < 18) {
  cout << "Good day.";
} else {
  cout << "Good evening.";
}

// shorthand :--
int time = 20;
string result = (time < 18) ? "Good day." : "Good evening.";
cout << result;

int a = 200;
int b = 33;
int c = 500;

if (a > b && c > a) {
  cout << "Both conditions are true";
}

switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}

int day = 4;
switch (day) {
  case 1:
    cout << "Monday";
    break;
  case 2:
    cout << "Tuesday";
    break;
  case 3:
    cout << "Wednesday";
    break;
  case 4:
    cout << "Thursday";
    break;
  case 5:
    cout << "Friday";
    break;
  case 6:
    cout << "Saturday";
    break;
  case 7:
    cout << "Sunday";
    break;
}
// Outputs "Thursday" (day 4)


int countdown = 3;

while (countdown > 0) {
  cout << countdown << "\n";
  countdown--;
}

cout << "Happy New Year!!\n";

do {
  // code block to be executed
}
while (condition);


#include <iostream>

using namespace std;
    
    int main() {
        int x ;
        cout << x << "\n";
        cin >> x ;
        cout << x << endl;
        cout << x << endl;
        
    }

    

 Derived Data Types in C++
 1. AArrya 
 2. Pointers
 3. rference
 4. fucntion

 Array - 
 arr1 = {1,2,3,4}

 pointers. - points to the memory address value
 int* i = &x

 reference - point to the memory location call by ref
 x = &y 


User defined datatypes: --

Class 
Structure
union
typedef
using

structure - to create a table or DB
 struct student {
  string name: kitty
  int age: 29;

 };



class - 
category which incorporated all function and data in single unit

class student {
  punlic:
   string name;
   int age; 
   };

Union

union allows member to share same memlocation
 union Data{
  int i;
  float f;
 };



sixze of datatypes 
char 1 byte
bool 1 byte
float 4
int 4 
double 8

// name canc only contain a underscore in special cahr
// start with underscore
// case sensitive
//garbagee value 

// Ternary operator

#include <bits/stdc++.h>

using namespace std;
int main()
{    
    int x = 0;
cout << ((x < 0) ? "less than zero" : ((x == 0) ? "itz zero" : "not zero" )); # nested ternary
}

 # Heap emmory/Dynamic / Malloc  -- Read dynamic memory 
 
 map - is a type of heap memory , dictionary
 Memoory leak saving. OOM/Memory exceeded error
 > delete ptr 
 Memory allocated with new should be deleted else it will block memory space
 linked list , tree, graph, dynamic arrays

 #When needed beyond function
 # Dangling pointer -- points to deallocated memory
 # Double deletion error.
 # placemnent new object in allocated memory

 # Use of Template and Define
 > ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0); --- 
 






