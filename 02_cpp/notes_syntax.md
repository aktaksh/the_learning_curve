# C++ syntax and memory — quick refresher

## Minimal program and input
```cpp
#include <iostream>
#include <string>

int main() {
    int x{};                       // initialise before use
    if (!(std::cin >> x)) return 1;
    std::cout << x << '\n';
}
```

Do not read an uninitialised local int. Identifiers are case-sensitive; prefer ordinary descriptive names and avoid reserved underscore forms.

## Types and initialisation
| Type | Reminder |
| --- | --- |
| int | Integer; width is implementation-dependent |
| double | Floating point |
| char | Character; sizeof(char) is always 1 |
| bool | true/false; default stream output is 1/0 |
| std::string | String value with automatic resource management |
| auto | Deduces a type from the initializer |

Common platforms use 4-byte int/float and 8-byte double, but do not treat those sizes as universal. Use sizeof and fixed-width integer types when appropriate. ASCII-based execution encodings map 65 to A; this is not a universal character-encoding rule.

## Operators
- Arithmetic: +, -, *, /, %. Integer division truncates toward zero.
- Assignment: =, +=, -=, *=, /=, %=.
- Comparison: ==, !=, <, <=, >, >=.
- Logical: &&, ||, !. && and || short-circuit.
- Bitwise: &, |, ^, ~, <<, >>.
- Precedence: 2 + 3 * 4 is 14; (2 + 3) * 4 is 20.

Avoid invalid shift counts, division by zero and signed overflow.

## Conditions and loops
```cpp
int hour = 16;
std::string greeting = hour < 12 ? "Morning" : "Later";

if (hour < 12) {
    std::cout << "Morning";
} else if (hour < 18) {
    std::cout << "Afternoon";
} else {
    std::cout << "Evening";
}

for (int i = 0; i < 3; ++i) std::cout << i;
while (hour > 0) --hour;
do { ++hour; } while (hour < 1);

switch (hour) {
    case 1: std::cout << "One"; break;
    default: std::cout << "Other"; break;
}
```

A do/while executes its body at least once. Missing break can fall through to the next switch case. Prefer if/else over deeply nested ternaries.

## Strings, arrays, pointers and references
```cpp
std::string full = std::string("John") + " Doe";
int values[] = {1, 2, 3, 4};
int x = 5;
int* pointer = &x;       // stores an address
int& reference = x;     // alias bound to x
*pointer = 6;           // updates x
reference = 7;          // also updates x
```

Pointers can be null or reassigned. References must be initialised and do not reseat. A function parameter of type int& can modify the caller's object. An array and a pointer are not the same type.

## Structs, classes, unions and aliases
```cpp
struct Student {
    std::string name;
    int age{};
};

class Counter {
public:
    void increment() { ++value_; }
private:
    int value_{};
};

union Data {
    int i;
    float f;
};

using Count = unsigned int;
```

A struct is a record type, not a database. Struct members default to public; class members default to private. Union members share storage; track the active member. using and typedef introduce type aliases. Templates generate code for parameterised types or values; macros perform preprocessing substitution.

## Memory and ownership
- Local automatic objects are destroyed at scope exit. Dynamic storage can outlive a function.
- Prefer containers and RAII owners such as std::vector and std::unique_ptr.
- Match new with delete, new[] with delete[], and malloc with free.
- A dangling pointer refers to an object whose lifetime ended. Double deletion and use-after-free are invalid.
- A leak loses the ability to release owned resources. It can contribute to memory exhaustion.
- std::map is an ordered associative container; it is not a synonym for heap memory.
- Placement new constructs an object in existing storage; storage ownership remains a separate responsibility.

Linked lists, trees and graphs often use dynamic storage. Pointer chasing can hurt cache locality; contiguous arrays/vectors can be better for hot paths.

## Stream performance
```cpp
std::ios_base::sync_with_stdio(false);
std::cin.tie(nullptr);
```

These settings decouple C++ streams from C stdio synchronisation and untie input from automatic output flushing. Flush prompts explicitly when needed; avoid assuming safe ordering when mixing C and C++ I/O.
