#FUNCTIONS
#named blocks of code that do a specific job
#Vending Machine: put in a # (input), machine processes(function), then drops snack down(output)
#You don't have to write code over and over or copy/paste bcuz u can reuse. Write once, name, reuse.

#Two Phases to a function

#Phase 1 - Define the function - These are the instructions for what this function should do
#Python stores instructions in memory

def greetings():
    print("hello!")
    
#Phase 2 - Call (run) the function by function_name()

# greetings() #python will execute the instructions

def make_coffee():  #def is the keyword for define - create a function then function_name then parentesis for input or perameters then colon lets python konw that the body is starting
    print("Grind coffee bean") #indent means this belongs to the function above. no indent means it doesn't belong to that
make_coffee() #calls or runs the function

#PERAMETERS AND ARGUMENTS

#imagine u r at a restaurant that serves tacos. waiter asks what kind of meat do u want? (the question is the peratmeter). you answer chicken - that's the argument.  
# #Perameter is a placeholder
def echo(message): #--->empty variable waiting for data a placeholder, the perameter (message)
    print(message)
#argument = Actual Value --> what u are putting inside the function in the function call ("hello" is value. chicken is the value from example above)
echo("Hello")

#why do perameters matter? bcuz w/o them, functions are stuck doing one thing.
#example
def say_name():
        print("Amy")
say_name()  #you can't put a value here. u had to put the value above in the function "Amy"

def double(number):
        print(number * 2)
double(5)

#Functions can have multiple perameters
def introduce(first_name, last_name):
    print("Hello " + first_name + " " +last_name)
introduce("Jael", "Bennett")

#Function Calling a Function
def login():
    print("Logging in...")
def load_dashboard():
    print("Dashboard loaded")
login()
load_dashboard()

#Function inside of a Function, Nested Function
def outer_function():
    def inner_function():
        print("I am inside")
    inner_function()
outer_function()  #calling the function

#Another nested function example - Global Scope which is where the variable is accessible
def outer(name): #global scope / outter function
    def inner(): #inner function has zero peramters bcuz inner function can see the outer function - called scope so it borrows the outer functions perameter
        print(f"Hello {name}")
    inner()
outer("Amy") #calling an outter function from the global scope

#SCOPE - the area where a variable is accessible

#Global Variable - a variable that is created outside the function and belongs to the entire program

favorite_food="Pizza" #created outside the function and avail to whole program.

def talk_about_food(): #this is LOCAL SCOPE and can only be used inside the function
        print(favorite_food) #you can use this bcuz it can see favorite_food at the global level, print is the instruction to display my favorite food
talk_about_food()  #if you don't do this line it does not exist!!  

#Python looks for LOCAl variable first then GLOBAL variable next
#LOCAL variable is created INSIDE your function

def classroom():
    student_name = "Amy" #variable i created
    print(student_name) #has to be local for a local variable
classroom() #function call
#if you want to call favorite_food right now you can because favorite_food is GLOBAL and you will get "pizza." It exsists outside the local function so it's accessible

#Can have a local and global function together

animal="Dog"  #global variable

def zoo():  #define the function "zoo" with empty perameter
    animal="Lion" #local variable only avail inside the function
    print(animal)  #will print lion bcuz python reads local variables first
zoo() #calling the function so you can pass an argument into the zoo(perameter)
print(animal) #Will print Dog

#Change the global variable with a global keyword

score = 0 #global variable whos value is held in memory

def increase_score(): #function that doesn't do anything yet but sets instructions
    global score #Normally, variables inside the function are local but we told this one to use the global instead.
    score = score + 1 #1st pass Python reads this as score = 0 + 1 bcuz it refers to the global variable. 
increase_score() #function call which runs the function process (0+1=1 and updates in memory score=1)
print(score) #creates output with the value of score which is now 1.

#PERAMETERS are also local variables

#i didn't really catch this part of the notes. read up on my own.

def make_message(message): #message perameter is local to the function
    def print_message():
        print(message) #since we have print inside outter function so it can access outside
    print_message()
make_message("Python is fun!")