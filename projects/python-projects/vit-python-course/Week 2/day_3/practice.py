# ITP Week 2 Day 3 (In-Class) Practice

# 1. 
    # a. run the following function and examine the behavior of the function return

# def print_greeting():
#     greetings = "hello"
#     print(greetings)

# # run it here!
print_greeting()

     
    # b. Convert this implicit return function to an explicit return function!

def return_greeting():
    greetings = "salutations"
    # CHANGE LINE BELOW
    # print(greetings)
    # CHANGE LINE ABOVE
    return greetings
    # c. Run the newly printed code! (Examine NOTHING is printed to the terminal!)
 #Confirmed - that was confusing. lol
# run it here!

    # d. Create a variable my_greeting and store the return value of return_hello then print the variable!

my_greeting = return_greeting()
print(my_greeting)