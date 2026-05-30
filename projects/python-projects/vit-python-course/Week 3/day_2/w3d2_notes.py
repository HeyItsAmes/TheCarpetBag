#JSON
#Serialization - taking a python object (json.dumps) and dumping python string into JSON object

import json
# #Nothing can read this butPython so Python has to translate this unless we import it import json
student = {
    "name":"Amy",
    "grade":100
}
json_data=json.dumps(student)
print(json_data)
print(type(json_data))

# #Deserializaton = json.loads ->you are loading json string into python object
text = '{"name":"Amy"}'
data=json.loads(text)
print(data["name"])
print(type(data))

#Pretend we have an API now - code below is wrong for some reason though, i get an error
response = '{"name":"Rick","status":"alive"}' #what python would receieve if you had an API
character = json.loads(response)
print(character.get("name"))

#Application Programming Interface API
#It's how you're able to send info over the internet
#You are a customer. Kitchen is db or server. Waiter is API
#^Working with an API is the same way as ordering food at a restaurant

#Using Python to Fetch API Data
import requests  #requests gives python the library to make requests

url="https://jsonplaceholder.typicode.com/posts"  #where we are storing our API address

response  = requests.get(url)
print(response) #if you get 200 in terminal that means it worked

#I want to be able to use the data now:
json_data=response.json()  #take json from API and convert it to python data. serialization

#API is a list of dictionaries now that it's converted from json objects to python dictionaries

for post in json_data[:5]:  #5 limits the amt returned to just 5 posts
    print(post.get("title")) #return the titles and the posts

