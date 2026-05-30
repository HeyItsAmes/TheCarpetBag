import requests  # HTTP library that simplifies the process of HTTP requets in order to interact w/ websites and api's
import json  # python json module toolbox & translates filetypes

state_url = "https://state-data-api.proxy.beeceptor.com/state-details"
travel_url = "https://state-data-api.proxy.beeceptor.com/state-travel-data"

# Test the APIs using a get request
state_response = requests.get(state_url)
travel_response = requests.get(travel_url)

# check the results of your request with a response
# state_response is a variable that stores what the server sends bk after HTTP request like get or post
# .status_code is a property of the info sent bk (object). It holds a 3 digit integer respresenting the servers status

# print(state_response.status_code) #200 means success
# print(travel_response.status_code) #200
# print(type(state_url))
# print(type(travel_url))

# 4. convert a JSON string into a Python object such as a dict or a list
state_data = json.loads(state_response.text)
travel_data = json.loads(travel_response.text)
# print(state_data)
# print(travel_data)
# print(type(state_data))  # class = list
# print(type(travel_data))  # class = list
#json.loads() converts the raw text into a Python object (like a dictionary), json.dumps() converts it back into a string that is formatted for readability. Use json.dumps to convert the python obj (dict) into a readable string

# Pretty-print to the console cuz no one can read that ish
print(json.dumps(state_data, indent=4))
print(json.dumps(travel_data, indent=4))
#conclusion: both datasets have a common column called "state"

# 5. merge datasets by "state" step by step:  IF state names matchco, combine them into one record

# combined_data = []
# # Take one state record, then search every travel record looking for a matching state name...
# for state in state_data:
#     for travel in travel_data:
#         print(state["state"], travel["state"])  #output: comparison of both state columns

#         # IF statement so it only does something with state names that match
#         if state["state"] == travel["state"]:
#             # if state and travel names are equal then print...
#             # print(state["state"], "DING! DING! ITS A MATCH")

#             # Above we printed it, now we are going to actually merge data and store it
#             # We already created combined_data = [] before the loops.
#             # new merged data is stored in combined_record
#             combined_record = {
#                 "state": state["state"],
#                 "region": state["region"],
#                 "population": state["population"],
#                 "top_attraction": travel["top_attraction"],
#                 "average_trip_cost": travel["average_trip_cost"],
#             }

#             combined_data.append(combined_record)

# # print(combined_data[:1])