W1D4 Lesson
📘 Week 1 – Day 4 Lesson
Modify lists and practice looping with while, for, and range().

Review Day 3 Exercise
We’ll start by briefly reviewing the previous day’s exercise to reconnect lists, booleans, and conditions before moving into today’s topics.

Change List Items
A list in Python is like a collection of items. You can change items in the list by using their index number.

Change One Item
Each item in a list has a position number (index). Indexes start at 0 (the first item).

fruits = ["strawberry", "blackcurrant", "watermelon", "orange", "kiwi", "melon", "mango"]

# Change the first item (index 0) to "grapefruit"
fruits[0] = "grapefruit"

print(fruits)
Change a Range of Items
You can replace several items at once by selecting a range with start:end.

fruits = ["strawberry", "blackcurrant", "watermelon", "orange", "kiwi", "melon", "mango"]

# Replace index 1 and 2 with "lemon" and "candy"
fruits[1:3] = ["lemon", "candy"]

print(fruits)
Working with Python Lists
Lists in Python can add, insert, extend, and remove items.

Add Items
1. Append to the End
Use .append() to add one item to the end of the list.

sports = ["football", "soccer", "baseball"]

sports.append("lacrosse")
print(sports)
2. Insert at a Position
Use .insert(index, item) to add an item at a specific spot.

sports.insert(1, "basketball")
print(sports)
3. Extend with Another List
Use .extend() to add all items from one list into another.

more_sports = ["hockey", "water polo"]

sports.extend(more_sports)
print(sports)
Remove Items
1. Remove by Value
Use .remove(item) to delete a specific item.

car_make = ["BMW", "Honda", "Mazda", "Ford", "Ronald Car"]

car_make.remove("Ronald Car")
print(car_make)
2. Remove by Index
.pop(index) removes the item at a given position.
If no index is given, .pop() removes the last item.
car_make.pop(0)   # removes "BMW"
car_make.pop()    # removes last item ("Ford")
print(car_make)
3. Delete with del
Use del to remove by index. If you don’t give an index, it deletes the whole list.

del car_make[0]   # removes "Honda"
print(car_make)   # ["Mazda"]

del car_make      # deletes the entire list
print(car_make)   # ❌ ERROR (list is gone – NameError)
4. Clear the List
Use .clear() to empty the list (but keep the variable).

long_list = ["a", "b", "c"]
long_list.clear()
print(long_list)  # []
Summary (List Methods)
.append() → add to end
.insert() → add at a position
.extend() → add multiple items
.remove() → remove by value
.pop() → remove by index (or last if no index)
del → remove by index OR delete whole list
.clear() → empty list but keep it
Strings behave like lists of characters, but you can’t change them directly (they’re immutable).
Practice
Instructions for today’s list practice are inside your practice.py file.

Python Loops
Python has two main types of loops:

while loops → repeat while a condition is true.
for loops → repeat for each item in a sequence.
while Loops
A while loop runs as long as the condition is True.

my_age = 16

while my_age < 21:
    print("waiting one more year")
    my_age += 1

# This loop stops once my_age reaches 21
Infinite Loop Example
If the condition is always true, the loop never ends:

while True:
    print("It's alive!")
To avoid infinite loops, always make sure something inside the loop changes the condition.
💡 In a terminal, you can usually stop an infinite loop with Ctrl + C.

while Loop with Indexing
We can use a counter (often called an iterator or “index variable”) to loop through a list:

new_list = ['a', 'b', 'c']
iterator = 0

while iterator < len(new_list):
    print(new_list[iterator])
    iterator += 1

# Prints every element in new_list
for Loops
A for loop is easier when working with lists. It goes through each item automatically.

names = ["Dan", "John", "Chuck", "Bob"]

for name in names:
    print("Hello " + name)
# Much simpler than writing 4 separate print statements.
Example with Numbers
numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number + 5)
# Each number is increased by 5.
for Loop with Any List
any_list = ["Hello", "World"]

for element in any_list:
    print(element)
# Variable names like element, item, or x are just placeholders.
Empty for Loops
Python does not allow completely empty loops. If you don’t want it to do anything yet, use pass.

for x in [0, 1, 2]:
    pass
Loop Summary
Use while when you don’t know how many times you’ll loop (it depends on a condition).
Use for when you want to go through items in a list, string, or range.
Always make sure loops can end, or you’ll get an infinite loop.
PIP and Python range()
PIP (Python Package Installer)
Stretch / preview topic: You don’t need PIP yet for this course, but it’s useful to know it exists.

Check if pip is installed:

pip --version
If you see a version number, pip is installed.

If not, one common approach is:

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

# Or on some systems:
python3 get-pip.py
Then check again with pip --version.
💡 Exact steps can vary by system. In real projects, you’ll follow the official docs for your operating system.

Python range()
The range() function creates a sequence of numbers that you can loop through.

1. Basic Usage
By default, range(n) starts at 0 and stops before n.

for x in range(6):
    print(x)
# 0, 1, 2, 3, 4, 5  (notice it stops at 5, not 6)
2. Custom Start and End
You can choose where to start and stop:

for x in range(2, 6):
    print(x)
# 2, 3, 4, 5
3. Custom Step (Increment)
You can also set how much to count by:

for x in range(2, 30, 3):
    print(x)
# 2, 5, 8, 11, ... 29
4. Using range() with Lists
You can loop through the indexes of a list:

starter_pokemons = ['charmander', 'squirtle', 'bulbasaur']

for i in range(len(starter_pokemons)):
    print(i)                     # index
    print(starter_pokemons[i])   # value
# This prints both the index and the Pokémon name.
5. else and break with Loops (advanced preview)
break → stop the loop early.
else → run code after the loop finishes normally (without a break).
for x in range(5):
    if x == 3:
        break
    print(x)
else:
    print("Loop finished!")  # Won’t run because of break
range() Summary
range(n) → 0 to n-1
range(start, stop) → from start to stop-1
range(start, stop, step) → count by step
Works great with lists when you want to use indexes.
Retrospective
We’ll close the day by talking about:

Which list operations you found easiest or hardest.
Whether for or while loops feel more natural right now.
Any “aha” moments you had working with range() and indexes.
Be ready to share one thing that clicked and one thing that still feels fuzzy.