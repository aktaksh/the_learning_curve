#include <iostream>
#include <string>

using namespace std;

struct Process {
    int pid;
    string name;
    double memoryMB;
};


int main()
{
    Process nginx;
     nginx.pid = 1254;
     nginx.name = "nginx";
     nginx.memoryMB = 34.7;

     cout << "PID :" << nginx.pid << "\n" <<  nginx.name << "\n"<< nginx.memoryMB << endl;
    cout << "size :" << sizeof("processautomation")<<endl;
    cout << &nginx << endl << &nginx.memoryMB <<endl << &nginx.name << endl;

    Process backup = nginx;
    backup.name = "apache";
    cout << "backup: " << backup.name << endl << backup.pid << endl;

}   
/*
===============================================================================
MODULE 1 : STRUCT vs CLASS
Real-world Example : Linux Process Information
===============================================================================

Example Use Case
----------------
Imagine writing a simplified version of Linux commands like:
- ps
- top
- htop

Every process has information such as:
- PID
- Process Name
- Memory Usage

We group these related pieces of data into a struct.

===============================================================================
QUESTIONS & ANSWERS
===============================================================================

Q1. Where is 'Process nginx;' stored?

Answer:
--------
Since it is declared inside main(), it is a local variable.

It is allocated on the STACK.

The std::string object itself is stored inside the struct on the stack.

The characters managed by std::string are usually stored on the HEAP
(unless Small String Optimization keeps very short strings inside the object).

===============================================================================

Q2. Why use a struct instead of separate variables?

Answer:
--------
Instead of:

int pid;
string name;
double memoryMB;

we group logically related information together.

Advantages:
- Better readability
- Easier maintenance
- Easier to pass around
- Represents a real-world object

Linux kernel heavily uses structs.

Examples:
- task_struct
- inode
- file
- socket

===============================================================================

Q3. Is a struct slower than using separate variables?

Answer:
--------
No.

The compiler simply places the members together in memory.

There is essentially no runtime overhead.

Structs are simply grouped variables.

===============================================================================

Q4. Why is sizeof(Process) sometimes larger than the sum of its members?

Answer:
--------
Because of MEMORY ALIGNMENT and PADDING.

Example:

int        -> 4 bytes
string     -> 32 bytes
double     -> 8 bytes

Expected:
44 bytes

Actual:
Often 48 bytes

The compiler inserts padding so that the CPU can access memory efficiently.

We'll study alignment in detail later.

===============================================================================

Q5. What happens when main() finishes?

Answer:
--------
When main() exits:

1. Process object goes out of scope.
2. Destructor for Process is called.
3. Destructor of std::string is called automatically.
4. Heap memory owned by std::string is released.

This automatic cleanup is called RAII
(Resource Acquisition Is Initialization).

===============================================================================

EXPERIMENT 1
Print Addresses
===============================================================================

Print:

&nginx
&nginx.pid
&nginx.name
&nginx.memoryMB

Question:
---------
Are these addresses close together?

Answer:
--------
Yes.

Struct members are stored contiguously in memory.

The compiler may insert padding between members.

===============================================================================

EXPERIMENT 2
Copying a Struct
===============================================================================

Question:
---------
If we write:

Process backup = nginx;

and modify:

backup.name = "apache";

Will nginx change?

Answer:
--------
No.

A new Process object is created.

std::string performs a deep copy.

The two objects become completely independent.

===============================================================================

EXPERIMENT 3
Stack Direction
===============================================================================

Create:

Process p1;
Process p2;

Print:

&p1
&p2

Question:
---------
Which direction does the stack grow?

Answer:
--------
On most x86-64 Linux systems,
the stack grows downward (towards lower memory addresses).

This is implementation