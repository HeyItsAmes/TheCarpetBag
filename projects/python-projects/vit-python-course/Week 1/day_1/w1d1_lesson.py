W1D1 Lesson
Week 1 – Day 1 Lesson
Print, strings, comments, variables, and user input.

1. The print() Function
In Python, the print() function is used to display information on the screen. It’s one of the first and most important functions you’ll learn because it lets you see what your code is doing.

What does print() do?
When you call print(), Python sends (or outputs) the information you give it to the terminal or console window.

Common uses:

Checking results: see what values your code is producing.
Communicating with users: display messages or instructions.
Debugging: check whether your code is working as expected.
Example:

print("Hello, world!")
You can print numbers, text, or a mix of both:

print(42)
print("The answer is", 42)
💡 Note: Anything inside quotes is treated as text (a string). Numbers without quotes are treated as numeric values.

2. Strings
A string is a sequence of characters – basically, text. In Python, strings are written inside single quotes (' ') or double quotes (" ").

Examples:

'Hello'
"Python"
"That's my favorite book."
'He said "What is your name?"'
There is no functional difference between single and double quotes for simple strings. You mainly switch depending on which quote you need inside the text.

Multi-line Strings
Sometimes you want text to span multiple lines. There are two common ways to do this.

1. Using \n (newline escape character)
The backslash (\) is used for escape sequences inside strings. \n means “start a new line”.

print("Line 1\nLine 2\nLine 3")
2. Using triple quotes (''' or """)
Triple-quoted strings allow you to write text across multiple lines exactly as you type it.

print("""This is line 1.
This is line 2.
This is line 3.""")
3. Comments
A comment is a note in your code that Python ignores when the program runs. Comments are for humans: they explain why the code is written a certain way or what it is supposed to do.

Single-line comments start with #:

# This is a comment line.
# Python skips this when executing.

print("This will run.")  # This is an inline comment
Keyboard shortcuts for toggling comments in VS Code
Windows: Ctrl + /
Mac: Cmd + /
💡 Tip: Use comments to leave yourself notes about tricky logic or assumptions. “Future you” will be grateful.

4. Variables
In Python, variables are names that store values such as text, numbers, or other data. You can think of a variable as a labeled box that holds something you want to reuse later.

Creating a variable
You create a variable by assigning a value using a single equals sign (=).

my_variable = "a string"
age = 25
pi = 3.14
Here:

my_variable, age, and pi are variable names.
The values ("a string", 25, 3.14) are stored inside them.
The = sign assigns the value to the variable.
Python does not require a keyword like var or let. A variable comes into existence as soon as you assign a value to it. Python also figures out the data type for you based on the value you assign.

Rules for naming variables
Must start with a letter or underscore (_).
Cannot start with a number.
Can only contain letters, numbers, and underscores (A–Z, a–z, 0–9, _).
Are case-sensitive (age, Age, and AGE are different).
Valid examples:

my_name = "Jaël"
_name = "Andre"
name1 = "Student"
Invalid examples:

1name = "error"     # starts with a number
my-name = "error"    # contains a hyphen
Multi-word variable names
When a variable name includes more than one word, you can format it in several styles. In Python, snake_case is the standard.

Style	Example	Description
PascalCase	MyFavoriteBand	Each word starts with a capital letter.
camelCase	myFavoriteBand	First word lowercase, following words capitalized.
snake_case	my_favorite_band	Words separated by underscores. Preferred in Python.
Example (recommended style):

my_favorite_band = "Coldplay"
Printing variables
You can use print() to see the contents of a variable.

name = "Danny"
print(name)
5. User Input with input()
The input() function lets your program receive information from the user. It shows a prompt, waits for the user to type something, and then returns that text as a string.

Example:

user_age = input("What is your age? ")
print("Wow, you look good for " + user_age)
How it works:

input() shows the prompt text: "What is your age? "
The user types a response and presses Enter.
The response is stored in the variable user_age as a string.
print() then displays a message that includes their answer.
💡 Important: input() always returns text (a string), even if the user types numbers. Later, we’ll learn how to convert that text into numeric types like int and float.

6. Practice
For this lesson, you will work in two files:

practice.py – shorter guided tasks to reinforce each concept.
exercise.py – a slightly more involved exercise that combines print(), strings, comments, variables, and input().
Detailed instructions are provided inside each file. Read the comments carefully and follow the prompts.