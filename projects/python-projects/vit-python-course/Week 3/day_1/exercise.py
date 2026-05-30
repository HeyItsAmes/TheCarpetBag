# ITP Week 3 Day 1 Exercise

# ENUMERATE!

# 1. Read all instructions first!
# 
# Prompt: given a list of names, create a list of dictionaries with the index as the user_id and name

users_list = ["Alex", "Bob", "Charlie", "Dexter", "Edgar", "Frank", "Gary"]
# examp_dict={
#     "key":"value"
# }
#each curly braces would be a standalone dictionary
# [
#     {
#         "user_id":0,
#         "name":"Alex"
#     },
#     {
#         "user_id":1,
#         "name":"Bob"
#     },
#     {
#         "user_id":2,
#         "name":"Charlie"
#     },
#     {
#         "user_id":3,
#         "name":"Dexter"
#     },
#     {
#         "user_id":4,
#         "name":"Edgar"
#     },
#     {
#         "user_id":5,
#         "name":"Frank"
#     },
#     {
#         "user_id":6,
#         "name":"Gary"
#     }
# ]
# example output    
# [{"user_id": 0, "name": "Alex"}, etc, etc]

# 1a. Create a function that takes a single string value and returns the desired dictionary
# def function_name(perameter to receive data):
#This function is going to create the dictionary

def create_user(user_id, user_name): #holds values
    # A dictionary defined inside the function
    return {
        "user_id": user_id,  # Using the parameter as a value
        "name": user_name, 
    }
# 1b. Create a new empty list called users_dict_list

users_dict_list=[]  #stores the results

for index, name in enumerate(users_list):

# 1c. Loop through users_list that calls the function for each item and appends the return value to users_dict_list
    users_dict_list.append(create_user(index, name))

# 2. Prompt: Given a series of dictionaries and desired output (mock_data.py), can you provide the correct commands?
from mock_data import mock_data
# print(type(mock_data))  #<class 'dict'>
# print(mock_data)
# print(mock_data.keys())
print(mock_data["results"][0])

# 2a. retrieve the gender of Morty Smith
#loop through the characters to find "name" is "Morty Smith" then retrieve "gender"

#go into the dictionary one at a time
for character in mock_data["results"]: 
    #chk to see if this "name" is "Morty Smith"
    if character["name"] == "Morty Smith":
        print(character["gender"])

# 2b. retrieve the length of the Rick Sanchez episodes

#go into the dictionary one at a time
for character in mock_data["results"]: 
    #chk to find Rick Sanchez
    if character["name"] == "Rick Sanchez": 
        #send the length of the episodes
        print(len(character["episode"]))  #51

# 2c. retrieve the url of Summer Smith location

for character in mock_data["results"]: 
    #chk to see if name is Summer Smith
    if character["name"] == "Summer Smith": 
        #send the url
        print(character["location"]["url"]) 