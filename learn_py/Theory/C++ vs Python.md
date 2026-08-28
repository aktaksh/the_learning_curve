# Python vs C++ — Common Syntax Cheat Sheet

> Examples use **Python 3** and **modern C++ (C++17 or newer)**.

## 1. Program structure and basic syntax

| Task | Python | C++ |
|---|---|---|
| Program entry point | Code can run directly | `int main() { ... return 0; }` |
| End a statement | New line | Semicolon: `;` |
| Define a block | Indentation | Braces: `{ ... }` |
| Single-line comment | `# comment` | `// comment` |
| Multi-line comment | `'''text'''` or `"""text"""` (technically a string) | `/* comment */` |
| Import/include | `import math` | `#include <cmath>` |
| Namespace | `math.sqrt(9)` | `std::sqrt(9)` |

## 2. Variables and common types

| Task | Python | C++ |
|---|---|---|
| Integer | `age = 25` | `int age = 25;` |
| Large integer | Automatic arbitrary precision | `long long n = 10000000000LL;` |
| Decimal number | `price = 19.99` | `double price = 19.99;` |
| Boolean | `active = True` | `bool active = true;` |
| Character | `letter = "A"` | `char letter = 'A';` |
| String | `name = "Alex"` | `std::string name = "Alex";` |
| Constant | `PI = 3.14159` (convention only) | `const double PI = 3.14159;` |
| Automatic type inference | Dynamic by default | `auto value = 42;` |
| No value | `None` | `nullptr` for a pointer; `std::nullopt` for an optional value |
| Type conversion | `int("42")`, `str(42)`, `float(42)` | `std::stoi("42")`, `std::to_string(42)`, `static_cast<double>(42)` |
| Check type | `type(x)` or `isinstance(x, int)` | Usually known at compile time; `typeid(x).name()` when needed |

## 3. Input and output

| Task | Python | C++ |
|---|---|---|
| Print text | `print("Hello")` | `std::cout << "Hello\n";` |
| Print variables | `print(name, age)` | `std::cout << name << " " << age << '\n';` |
| Formatted output | `print(f"{name} is {age}")` | `std::cout << name << " is " << age << '\n';` |
| Read a string | `name = input("Name: ")` | `std::getline(std::cin, name);` |
| Read a number | `age = int(input("Age: "))` | `std::cin >> age;` |

> C++ note: after `std::cin >> value`, use `std::getline(std::cin >> std::ws, text)` to safely read a full line.

## 4. Operators

| Operation | Python | C++ |
|---|---|---|
| Assignment | `x = 5` | `x = 5;` |
| Add/subtract/multiply | `a + b`, `a - b`, `a * b` | `a + b`, `a - b`, `a * b` |
| True division | `a / b` | `static_cast<double>(a) / b` if `a` and `b` are integers |
| Integer division | `a // b` | `a / b` when both values are integers |
| Remainder | `a % b` | `a % b` |
| Power | `a ** b` | `std::pow(a, b)` |
| Equal / not equal | `a == b`, `a != b` | `a == b`, `a != b` |
| Logical AND | `a and b` | `a && b` |
| Logical OR | `a or b` | `a \|\| b` |
| Logical NOT | `not a` | `!a` |
| Increment | `x += 1` | `x++` or `++x` |
| Ternary expression | `x if condition else y` | `condition ? x : y` |
| Membership test | `x in items` | `std::find(items.begin(), items.end(), x) != items.end()` |

## 5. Conditions

| Python | C++ |
|---|---|
| `if x > 0:` | `if (x > 0) {` |
| `elif x == 0:` | `} else if (x == 0) {` |
| `else:` | `} else {` |
| Indented body | `    // body` is replaced by C++ statements inside braces |
| No closing keyword | `}` closes the block |

### Full example

| Python | C++ |
|---|---|
| `if score >= 90:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`grade = "A"`<br>`elif score >= 80:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`grade = "B"`<br>`else:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`grade = "C"` | `if (score >= 90) {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`grade = "A";`<br>`} else if (score >= 80) {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`grade = "B";`<br>`} else {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`grade = "C";`<br>`}` |

## 6. Loops

| Task | Python | C++ |
|---|---|---|
| Repeat 5 times | `for i in range(5):` | `for (int i = 0; i < 5; i++) {` |
| Range 1 through 5 | `for i in range(1, 6):` | `for (int i = 1; i <= 5; i++) {` |
| Range with step 2 | `for i in range(0, 10, 2):` | `for (int i = 0; i < 10; i += 2) {` |
| Loop over values | `for x in items:` | `for (const auto& x : items) {` |
| Index and value | `for i, x in enumerate(items):` | `for (std::size_t i = 0; i < items.size(); i++) { auto& x = items[i]; }` |
| While loop | `while condition:` | `while (condition) {` |
| Infinite loop | `while True:` | `while (true) {` |
| Stop loop | `break` | `break;` |
| Skip iteration | `continue` | `continue;` |

## 7. Functions

| Task | Python | C++ |
|---|---|---|
| Define a function | `def add(a, b):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return a + b` | `int add(int a, int b) {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return a + b;`<br>`}` |
| Call a function | `result = add(2, 3)` | `int result = add(2, 3);` |
| No return value | `def greet():` | `void greet() { ... }` |
| Default argument | `def greet(name="World"):` | `void greet(std::string name = "World") { ... }` |
| Multiple return values | `return x, y` | `return std::pair{x, y};` or `return std::tuple{x, y, z};` |
| Anonymous function | `square = lambda x: x * x` | `auto square = [](int x) { return x * x; };` |

## 8. Lists, arrays, and vectors

| Task | Python list | C++ vector |
|---|---|---|
| Create | `nums = [1, 2, 3]` | `std::vector<int> nums{1, 2, 3};` |
| Empty collection | `nums = []` | `std::vector<int> nums;` |
| Length | `len(nums)` | `nums.size()` |
| First item | `nums[0]` | `nums[0]` |
| Last item | `nums[-1]` | `nums.back()` |
| Add to end | `nums.append(4)` | `nums.push_back(4);` |
| Remove last | `nums.pop()` | `nums.pop_back();` |
| Insert | `nums.insert(i, value)` | `nums.insert(nums.begin() + i, value);` |
| Remove by value | `nums.remove(value)` | `nums.erase(std::remove(nums.begin(), nums.end(), value), nums.end());` |
| Slice | `nums[start:end]` | `std::vector<int>(nums.begin() + start, nums.begin() + end)` |
| Sort ascending | `nums.sort()` | `std::sort(nums.begin(), nums.end());` |
| Reverse | `nums.reverse()` | `std::reverse(nums.begin(), nums.end());` |
| Value exists | `value in nums` | `std::find(nums.begin(), nums.end(), value) != nums.end()` |

## 9. Dictionaries/maps and sets

| Task | Python | C++ |
|---|---|---|
| Create key-value collection | `ages = {"Ana": 20, "Ben": 25}` | `std::unordered_map<std::string, int> ages{{"Ana", 20}, {"Ben", 25}};` |
| Read or assign a value | `ages["Ana"]` | `ages["Ana"]` |
| Check for a key | `"Ana" in ages` | `ages.contains("Ana")` (C++20) or `ages.find("Ana") != ages.end()` |
| Loop over key and value | `for key, value in ages.items():` | `for (const auto& [key, value] : ages) {` |
| Create a set | `seen = {1, 2, 3}` | `std::unordered_set<int> seen{1, 2, 3};` |
| Add to a set | `seen.add(4)` | `seen.insert(4);` |
| Remove from a set | `seen.discard(4)` | `seen.erase(4);` |

## 10. Strings

| Task | Python | C++ |
|---|---|---|
| Length | `len(text)` | `text.size()` |
| Character at index | `text[i]` | `text[i]` |
| Substring | `text[start:end]` | `text.substr(start, length)` |
| Find text | `text.find("abc")` | `text.find("abc")` |
| Not found result | `-1` | `std::string::npos` |
| Join strings | `first + last` | `first + last` |
| Repeat string | `"ha" * 3` | Use a loop (no built-in `*` operator for strings) |
| Convert to upper case | `text.upper()` | Loop with `std::toupper` |
| Split words | `text.split()` | Usually use `std::istringstream` |

## 11. Classes and objects

| Python | C++ |
|---|---|
| `class Person:` | `class Person {` |
| `def __init__(self, name):` | `public:`<br>`Person(std::string name) : name(name) {}` |
| `self.name = name` | `std::string name;` |
| `def greet(self):` | `void greet() const {` |
| `return self.name` | `return` type must match, e.g. `std::string getName() const { return name; }` |
| No class terminator | Class ends with `};` |
| Create object: `p = Person("Ana")` | `Person p("Ana");` |
| Access member: `p.name` | `p.name` for an object, `ptr->name` for a pointer |

## 12. Exceptions

| Task | Python | C++ |
|---|---|---|
| Start protected block | `try:` | `try {` |
| Catch an error | `except ValueError as error:` | `catch (const std::invalid_argument& error) {` |
| Catch any standard error | `except Exception as error:` | `catch (const std::exception& error) {` |
| Raise/throw | `raise ValueError("message")` | `throw std::invalid_argument("message");` |
| Always execute | `finally:` | Use RAII/destructors; C++ has no `finally` keyword |

## 13. File handling

| Task | Python | C++ |
|---|---|---|
| Open for reading | `with open("data.txt") as file:` | `std::ifstream file("data.txt");` |
| Open for writing | `with open("data.txt", "w") as file:` | `std::ofstream file("data.txt");` |
| Read one line | `line = file.readline()` | `std::getline(file, line);` |
| Write text | `file.write("Hello\n")` | `file << "Hello\n";` |
| Close file | Automatic after `with` block | Automatic when the stream goes out of scope |

## 14. Common mix-ups to remember

| Python habit | C++ equivalent / warning |
|---|---|
| `True`, `False`, `None` | `true`, `false`, `nullptr` |
| `and`, `or`, `not` | `&&`, `\|\|`, `!` |
| `elif` | `else if` |
| `len(x)` | `x.size()` |
| `list.append(x)` | `vector.push_back(x)` |
| `for x in items:` | `for (const auto& x : items) { ... }` |
| `print(x)` | `std::cout << x << '\n';` |
| `input()` returns a string | `std::cin >> x` reads into the declared type |
| Indentation defines blocks | Braces `{}` define blocks; indentation is for readability |
| Variables can change type | Variables have a fixed type after declaration |
| Lists can mix types | `std::vector<T>` normally contains one declared type |
| Negative index: `items[-1]` | Use `items.back()`; `items[-1]` is invalid/unsafe |
| Integer division: `5 // 2 == 2` | `5 / 2 == 2`, but `5.0 / 2 == 2.5` |
| Chained comparison: `0 < x < 10` | Write `0 < x && x < 10` |
| `a is b` checks identity | Do not translate to `==` blindly; C++ object/pointer semantics differ |
| Automatic memory management | Prefer stack objects and smart pointers such as `std::unique_ptr` |

## 15. Headers commonly needed in C++

| Feature | Header |
|---|---|
| Input/output | `#include <iostream>` |
| Strings | `#include <string>` |
| Vectors | `#include <vector>` |
| Maps/sets | `#include <unordered_map>` / `#include <unordered_set>` |
| Algorithms such as sort/find | `#include <algorithm>` |
| File streams | `#include <fstream>` |
| String streams | `#include <sstream>` |
| Math functions | `#include <cmath>` |

### Minimal runnable examples

| Python | C++ |
|---|---|
| `name = input("Name: ")`<br>`for i in range(3):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`print(f"Hello, {name}!")` | `#include <iostream>`<br>`#include <string>`<br><br>`int main() {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`std::string name;`<br>&nbsp;&nbsp;&nbsp;&nbsp;`std::cout << "Name: ";`<br>&nbsp;&nbsp;&nbsp;&nbsp;`std::getline(std::cin, name);`<br>&nbsp;&nbsp;&nbsp;&nbsp;`for (int i = 0; i < 3; i++) {`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`std::cout << "Hello, " << name << "!\n";`<br>&nbsp;&nbsp;&nbsp;&nbsp;`}`<br>&nbsp;&nbsp;&nbsp;&nbsp;`return 0;`<br>`}` |
