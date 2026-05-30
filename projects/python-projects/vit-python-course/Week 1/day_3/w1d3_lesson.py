W1D3 Lesson
Week 1 – Day 3 Lesson: Booleans, Logic, and Lists
Today you’ll learn how Python makes decisions (True/False) and how to store multiple values in a list.

Booleans
In programming, we often need to check whether something is true or false. In Python, these values are represented by the Boolean type:

True
False
Evaluating Expressions
Comparison expressions evaluate to Boolean values:

print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
Each comparison returns either True or False.

The bool() Function
The built-in bool() function tells you whether a value is considered true or false in a Boolean context:

print(bool("Hello"))   # True  - non-empty string
print(bool(15))        # True  - non-zero number

print(bool(""))        # False - empty string
print(bool(0.0))       # False - zero
General rules:

Non-empty strings, non-zero numbers, and most non-empty objects → True.
Empty strings (""), zero (0, 0.0), and empty collections ([], {}, etc.) → False.
💡 You won’t use bool() every day, but it’s a good way to see how Python “thinks” about truthiness.

Comparison Operators
Comparison operators compare two values and return a Boolean result.

Operator	Meaning	Example
==	Equal to	x == y
!=	Not equal to	x != y
>	Greater than	x > y
<	Less than	x < y
>=	Greater than or equal to	x >= y
<=	Less than or equal to	x <= y
Example in Action
a = 4
b = 5
c = 5

print(a == b)  # False
print(b == c)  # True

print(a != b)  # True
print(b != c)  # False

print(a > b)   # False
print(b > c)   # False

print(a < b)   # True
print(b < c)   # False

print(a >= b)  # False
print(b >= c)  # True

print(a <= b)  # True
Logical Operators
Logical operators combine Boolean expressions. They also return True or False.

Operator	Description	Example
and	True if both statements are true	x < 5 and x < 10
or	True if at least one statement is true	x < 5 or x < 4
not	Reverses the result	not (x < 5 and x < 10)
and Example
a = 4
b = 5
c = 5

print(a > 2 and b == c)  # True and True → True
or Example
a = 4
b = 5
c = 5

print(a > 2 or b != c)   # True or False → True
not Example
light_switch_on = True
opposite = not light_switch_on
print(opposite)  # False
Summary of logical operators:

and → both conditions must be true.
or → at least one condition must be true.
not → flips the result.
Identity Operators (Preview)
Identity operators check whether two variables refer to the same object in memory, not just whether they have the same value.

Operator	Description	Example
is	True if both variables refer to the same object	x is y
is not	True if both variables do not refer to the same object	x is not y
Example with Numbers
age1 = 21
age2 = 21

print(age1 == age2)  # True  - same value
print(age1 is age2)  # Often True for small integers (same object)
Example with Dictionaries
obj1 = {"a": "b"}
obj2 = {"a": "b"}

print(obj1 == obj2)  # True  - values are equal
print(obj1 is obj2)  # False - different objects in memory
Key idea (for now):

Use == when you care about values.
is is a more advanced tool — you mostly need it when checking things like value is None.
💡 For this course, focus on == for comparisons. Identity is here as a preview so it’s not scary later.
If / Elif / Else Statements
So far, our code has run from top to bottom. if statements let us make decisions and run certain lines only when conditions are true.

Basic Structure
if condition:
    # code runs if condition is True
elif another_condition:
    # code runs if the first was False but this is True
else:
    # code runs if none of the above were True
Exactly one if per chain.
Zero or more elif blocks.
Zero or one else, and it must come last.
Example: Employee IDs
employee_id = 5048

if employee_id >= 9000:
    print("VIPs")
elif employee_id >= 8000:
    print("8th floor Executive")
elif employee_id >= 7000:
    print("7th floor Managers")
elif employee_id >= 6000:
    print("6th floor Sales")
elif employee_id >= 5000:
    print("5th floor Operations")
elif employee_id >= 4000:
    print("4th floor Communications")
elif employee_id >= 3000:
    print("3rd floor Logistics")
elif employee_id >= 2000:
    print("2nd floor Admin")
else:
    print("Lobby Security")
Python checks each condition in order. As soon as one is True, it runs that block and skips the rest.

Indentation Matters
if weather == "Raining":
    print("Grab an umbrella!")  # inside the condition
print("Leave for work")         # always runs (outside the if)
Example: Morning Routine
weather = "Sunny"

print("Wake up")
print("Brush teeth")
print("Get dressed")

if weather == "Raining":
    print("Grab umbrella!")
elif weather == "Gloomy":
    print("Might need a jacket")
else:
    print("No umbrella needed")

print("Leave for work")
Summary of control flow:

if → first condition to check.
elif → extra conditions if previous ones were false.
else → “everything else” case.
Python Collections (Overview)
Python has four main collection (data structure) types:

List → ordered, changeable, allows duplicates.
Tuple → ordered, unchangeable, allows duplicates.
Set → unordered, unindexed, no duplicates.
Dictionary → ordered (Python 3.7+), key/value pairs, changeable, keys unique.
For today, lists are the main focus. The other collection types are here so the names feel familiar later.

Lists
Lists store multiple items in a single variable. They are created using square brackets [].

my_list = ["apple", "banana", "cherry"]
Properties of lists:

Ordered → items have positions (indexes).
Changeable (mutable) → you can add, remove, or modify items.
Allow duplicates → repeated values are allowed.
Indexing (accessing items)
List items are indexed starting at 0:

fruits = ["apple", "banana", "cherry", "orange"]

print(fruits[0])  # "apple"
print(fruits[1])  # "banana"
Changing Items
fruits[1] = "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry", "orange"]
Lists with Different Data Types
list_1 = ["apple", "banana", "cherry"]
list_2 = [1, 5, 7, 9, 3]
list_3 = [True, False, False]
list_4 = ["abc", 34, True, 40, "male"]
list_5 = [["John", "Smith"], ["Jane", "Doe"], 123, False]
Useful Built-in Functions with Lists
print(type(list_5))        # <class 'list'>
print(len(list_5))         # number of items

# Using the list constructor with another iterable
list_6 = list(("apple", "banana", "cherry"))
print(list_6)
Access List Items (Positive Indexing)
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(fruits[0])  # "apple"
print(fruits[6])  # "mango"
print(fruits[4])  # "kiwi"
Negative Indexing
Negative indexes count from the end:

print(fruits[-1])  # "mango" (last item)
print(fruits[-2])  # "melon" (second to last)
Slice: Range of Indexes
Use slicing to get a sub-list: list[start:end] (end is not included).

print(fruits[2:5])   # ["cherry", "orange", "kiwi"]
print(fruits[:4])    # ["apple", "banana", "cherry", "orange"]
print(fruits[2:])    # ["cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[-4:-1]) # ["orange", "kiwi", "melon"]
Checking if an Item Exists
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")
Summary
Booleans → represent truth values: True or False.
Operators → compare values (==, <, >), combine conditions (and, or, not), or (later) check identity (is, is not).
If / Elif / Else → choose which code to run based on conditions.
Collections → List, Tuple, Set, Dictionary.
Lists → ordered, changeable, allow duplicates; accessed with indexes, slices, and the in keyword.


Google Python Class – ListsLinks to an external site.
W3Schools – Python ListsLinks to an external site.