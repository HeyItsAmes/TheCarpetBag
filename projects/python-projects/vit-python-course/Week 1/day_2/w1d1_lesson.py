W1D2 Lesson
📘 Week 1 – Day 2 Lesson: Data Types, Numbers, and Casting
Data types, numbers, assignment, and turning strings into numbers (and back again).

Heads up: this page shows you lots of types so you know what’s possible in Python. For everyday work in this course, you’ll mainly use str, int, float, bool, and later list and dict. The rest are “nice to know.”
1. Data Types
In programming, a data type defines the kind of value a variable can hold and what operations you can perform with it.

Python comes with several built-in data types, organized into categories:

Category	Types
Text Type	str
Numeric Types	int, float, complex*
Boolean Type	bool
Sequence Types	list, tuple*, range
Mapping Type	dict
Set Types	set, frozenset*
Binary Types	bytes*, bytearray*, memoryview*
*Starred types are more advanced. We’ll mention them briefly now and revisit later (or in your own exploration).

2. Variables and Data Types (Continuation)
Variables in Python can store different types of data. When you assign a value to a variable, Python automatically decides its type.

Examples:

Example	Data Type
x = "Hello World"	str
x = 20	int
x = 20.5	float
x = True	bool
x = ["apple", "banana", "cherry"]	list
x = range(6)	range
x = {"name": "John", "age": 36}	dict
x = 2 + 3j	complex*
x = ("apple", "banana", "cherry")	tuple*
x = {"apple", "banana", "cherry"}	set
x = frozenset({"apple", "banana", "cherry"})	frozenset*
x = b"Hello"	bytes*
x = bytearray(5)	bytearray*
x = memoryview(bytes(5))	memoryview*
Checking the Type of a Variable
You can always check what type Python assigned by using the type() function:

print(type("Hello"))

example_num = 34.0
print(type(example_num))
3. Numbers
Python has three main numeric types:

Integers: int
Whole numbers, positive or negative, without decimals:

x = 42
y = -10
z = 12345678901234567890  # Python can handle big integers

print(x, type(x))
print(y, type(y))
print(z, type(z))
Floating Point Numbers: float
Numbers with decimals, positive or negative:

pi = 3.14159
temperature = -12.5

print(pi, type(pi))
print(temperature, type(temperature))
Complex Numbers: complex (Preview)
Numbers with a real and an imaginary part, written with j for the imaginary part. These are common in certain math-heavy fields (engineering, signal processing, etc.).

z = 2 + 3j
print(z, type(z))
💡 For this course, you don’t need to use complex numbers. Just know they exist.

4. Arithmetic Operators
Python uses these operators to do basic math:

Operator	Name	Example
+	Addition	x + y
-	Subtraction	x - y
*	Multiplication	x * y
/	Division	x / y
%	Modulus (remainder)	x % y
**	Exponentiation (power)	x ** y
//	Floor division	x // y
Using Variables with Operators
We can store results of arithmetic operations inside variables:

# Addition
sum_result = 4 + 4
print(sum_result)

# Subtraction (can give negatives)
sub_result = 1 - 100
print(sub_result)

# Division (returns a float)
div_result = 10 / 5
print(div_result)

# Floor division (drops the decimal part)
floor_result = 10 // 3
print(floor_result)

# Modulus (remainder after division)
remainder = 10 % 3
print(remainder)

# Exponentiation (power)
power = 2 ** 5
print(power)
5. Modules and the round() Function
What Are Modules?
A module in Python is like a code library — a file that contains functions you can reuse. Modules save you from having to write the same code over and over again.

Python gives you:

Built-in functions like print(), input(), type().
The standard library — a collection of modules you can import when needed.
The round() Function
Python includes a built-in function called round() that rounds numbers. It takes one required argument (the number) and an optional second argument (how many decimal places).

number = 1.23456

print(round(number))      # 1    -> rounded to 0 digits (int)
print(round(number, 0))   # 1.0  -> 0 digits, returns float
print(round(number, 1))   # 1.2  -> 1 decimal place
print(round(number, 2))   # 1.23 -> 2 decimal places
print(round(number, 3))   # 1.235 -> 3 decimal places (last digit rounded up)
round() sometimes rounds up and sometimes down, depending on the last digit.

Importing Modules: math.ceil()
If you always want to round up, you can use the math module’s ceil() function.

import math

num = 4.3
print(math.ceil(num))   # 5
Unlike round(), math.ceil() always rounds up to the nearest whole number.

6. Updating Variables and Assignment Operators
Updating a Variable
You can update a variable instead of creating a new one:

x = 10
x = x + 5   # update the existing variable
print(x)    # 15
This keeps your code simpler and easier to read.

Assignment Operators
Assignment operators let us combine assignment and arithmetic in shorthand form.

Operator	Example	Same As
=	x = 5	x = 5
+=	x += 3	x = x + 3
-=	x -= 3	x = x - 3
*=	x *= 3	x = x * 3
/=	x /= 3	x = x / 3
%=	x %= 3	x = x % 3
**=	x **= 3	x = x ** 3
//=	x //= 3	x = x // 3
Example
# Start with a number
x = 3

# Add 6
x += 6
print(x)   # 9

# Behind the scenes:
# x = x + 6
# x = 3 + 6
# x = 9
7. Common Mistakes
1. Using a Variable Before Assigning It
y += 3
# NameError: name 'y' is not defined
2. Mixing Strings and Numbers
y = "3"
y += 3
# TypeError: can only concatenate str (not "int") to str
If you want to join a number to a string, convert it first:

y = "3"
y += str(3)
print(y)   # "33"
8. Casting (Changing Data Types)
What is Casting?
Casting means changing the type of data so Python can use it the way you want.

You can’t add a string "5" to a number 5 without converting one of them.
Python uses special functions called constructors to do this: int(), float(), str(), etc.
We’ll focus on the three most common casting functions.

int() → Convert to Integer (Whole Numbers)
The int() function turns something into a whole number.

Examples that work:

# From an integer (stays the same)
a = int(1)
print(a)   # 1

# From a float (decimal part is dropped, not rounded)
b = int(12.9)
print(b)   # 12

# From a string (if the string is a whole number)
c = int("15")
print(c)   # 15
Example that fails:

# This will cause an error because "12.5" isn't a whole number
d = int("12.5")
Use int() when you want to make sure a value is treated as a whole number.

float() → Convert to Decimal Numbers
The float() function turns values into numbers with decimals.

# From an integer
e = float(12)
print(e)   # 12.0

# From a float (stays the same)
f = float(12.5)
print(f)   # 12.5

# From a string that looks like a number
g = float("100")
print(g)   # 100.0

string_number = "12554.34"
print(float(string_number))  # 12554.34
Tip: if you’re not sure a string is safe to convert directly to int, you can try float first.

Example: casting a string with decimals:

num_str = "12.5"

# This will cause an error:
# print(int(num_str))

# First convert to float, then to int
num_float = float(num_str)  # 12.5
num_int = int(num_float)    # 12

print("As float:", num_float)
print("As int:", num_int)
str() → Convert to String (Text)
The str() function turns almost anything into text.

# From a string (no change)
h = str("hello")
print(h)

# From an integer
i = str(1)
print(i)   # "1"

# From a float
j = str(1230.45)
print(j)
Use str() when you need to display values in messages or build text output.

Other Casting Functions (For Reference)
bool() → turns values into True or False.
complex() → turns values into complex numbers (used in advanced math).
9. Example: User Input and Casting
When you ask for input, Python always gives you a string, even if the user types a number. If you want to do math, you must cast it first.

# Ask the user for their age
age = input("Enter your age: ")
print(type(age))   # <class 'str'>

# Cast to integer so we can add to it
age = int(age)
print("Next year, you will be", age + 1)
Without casting, "25" + 1 would cause an error. With casting, it works.

10. Quick Comparison
Function	What it does	Example Input	Example Output	When to Use
int()	Makes whole numbers	int("12")	12	Counting, IDs, ages
float()	Makes decimals	float("12.5")	12.5	Money, measurements, averages
str()	Makes text	str(99)	"99"	Printing and displaying values
In short:

int() → whole numbers.
float() → numbers with decimals.
str() → text.

Resources
Optional but recommended references if you want to dig deeper after class:

PyNative – Python Type CastingLinks to an external site.
Good explanations and examples for converting between data types.
W3Schools – Python CastingLinks to an external site.
Covers int(), float(), and str() with simple examples.
TutorialsPoint – Complex Numbers in PythonLinks to an external site.
For those curious about complex numbers and when they’re useful.
W3Schools – Python OperatorsLinks to an external site.
Quick reference for arithmetic and other operators.
Official Python Standard Library DocsLinks to an external site.
The official list of built-in modules that ship with Python.