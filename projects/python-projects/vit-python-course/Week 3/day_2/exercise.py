# ITP Week 3 Day 2 Exercise

# import in the two modules for making API calls and parsing the data

import requests  # make API calls
import json  # deserialization and serialization

# set a url variable to "https://rickandmortyapi.com/api/character"

url = "https://rickandmortyapi.com/api/character"

# set a variable response to the "get" request of the url#goes to the api and asks for data

response = requests.get(url)

# print to verify we have a status code of 200
# print(response.status_code)  #200 = success

# assign a variable json_data to the responses' json
# gives actual data (dictionary/list)
json_data = response.json()

# print to verify a crazy body of strings!

# print(json_data)

# lets make it into a python dictionary by using the appropriate json method
# response.text is a raw JSON string
# json.loads() is a python dictionary
# set it all to a variable called "data"

data = json.loads(response.text)

# print the newly created python object
# print(data)
print(type(data))
