# ITP Week 1 Day 4 Exercise

#lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 1. loop through the lowercase and print each element

# for letters in lowercase:
#     print(letters)

# 2. loop through the lowercase and print the capitalization of each element

# for letters in lowercase:
#     print(letters.upper())

# MEDIUM

# 1. create a new variable called uppercase with an empty list

# uppercase=[]

# 2. loop through the lowercase list
    # 2a. append the capitalization of each element to the uppercase list
    
# for letters in lowercase:
#     uppercase.append(letters.upper())
# print(uppercase)  #outside the loop to print letters as a full list.  Inside the loop would have given you one letter at at time.

# HARD

# A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.

# password = "MySuperSafePassword!@34"

# special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

# 1. create the following variables and assign them Booleans as False
# has_uppercase=False
# has_lowercase=False
# has_number=False
# has_special_char=False

# 2. loop through the string password (same as a list)
# OR you can create a new list variable of the string password
# using list(string) NOTE: assign it a new variable as such:
# password_list = list(password) prior to looping.

# for char in password:
#     print(char)  
# #outside the loop to print letters as a full list.  
# #Inside the loop would have given you one letter at at time

# 3. For each iteration of the loop, create a if statement
# check to see if it exists in any of the list by using IN
# if it does exist, update the appropriate variable and CONTINUE
# not break.
# # NOTE: to see if it has a number, use range from 0 - 10!

password = "MySuperSafePassword!@34" #user input to chk against in loop
special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']  #chk symbols against this list
has_uppercase=False  # Initialize flags
has_lowercase=False
has_number=False
has_special_char=False

for char in password:  #loop thru characters in password string #char holds ONE character from pword each time it loops
    if char.isupper():  #compare each letter in string to see if its uppercase
        has_uppercase=True #if so tell me yup
      
    elif char.islower():
        has_lowercase=True
             
    elif char in special_char:
        has_special_char=True
       
    for number in range(0,10):
        if char == str(number):
            has_number = True

# 4. do a final check to see if all of your variables are TRUE
# by using the AND operator for all 4 conditions. (This is done for you, uncomment below)

#Why is my freaking final_result false??
# print(has_uppercase)
# print(has_lowercase)
# print(has_number)
# print(has_special_char)

final_result = has_uppercase == True and has_lowercase == True and has_number == True and has_special_char == True

# NOTE: we can shorthand this by just checking if the variable exists (returns True)
#final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# this will fail the same if any one of them is False

if final_result == True:
print("Your password is fire!")
else:
print("Update password: its weak sauce")

# If the final_result is true, print "SAFE STRONG PASSWORD"
# else, print "Update password: too weak"
# NOTE: this must be done outside of the loop


# BONUS: update the password variable to take in an user input!

# password = input("Create a password that has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.")

# NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!
