# ITP Week 1 Day 2 Exercise

# BONUS 2: can you REFACTOR using less variables?
# use the same variable for each step so it updates each time rather than create a new variable at each step.

# We will replicate a number magic trick with Python! Below is the magic trick that we will convert! Below that is the python instructions, you will need to complete.

# Step 1: Pick a number from 1 - 9
# Step 2: Multiple by 2
# Step 3: Add 10 to the total
# Step 4: Divide by 2
# Step 5: Subtract by the original number
# Final Number: 5

# assign a variable "step_1" to a number of your choice between 1 - 9
#step_1=2  #2  FIRST ANSWER
# #BONUS ANSWER BELOW

user_input=int(input("Type a number to see a magic trick!"))

# #Take the users text input, convert it to a number, and store it in step_1

# # assign a variable "step_2" to the product of step_1 and the number 2
step=user_input*2  #4

# # assign a variable "step_3" to the sum of step_2 and the number 10
step=step+10   #14

# # assign a variable "step_4" to the quotient of step_3 and the number 2
step=step/2  #7

# # assign a variable "step_5" to the difference between step_4 and step_1
step=step-user_input  #5

# final_num=((step_1*2) +10)/2 - step_1

final_num=((step*2) +10)/2 - step
# print step_5 and you should see 5!
print(final_num)
