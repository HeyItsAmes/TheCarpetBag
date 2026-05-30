#json.dumps - turn python object into json text (serialization)
#json.loads - turn JSON text into python (deserialization)

import json

example_dict={
    "name":"Amy",
    "age":28,
    "city":"New York"
}

# result=json.dumps(example_dict)
# print(result)
# print(type(result))

#Indent - add spacing/pretty formatting , makes it better to read
indented_json = json.dumps(example_dict, indent=4)
print(indented_json)

#Seperators - allows us to change punctuation  default is :

seperated_json=json.dumps(example_dict, indent=4, separators=(".","="))
print(seperated_json)

#sort_keys=True 
#Sorts JSON keys alphbetically
print(json.dumps(example_dict, indent=4, sort_keys=True))

#Comining everything together

print(json.dumps(example_dict, indent=2, separators=(" ; ", " = "), sort_keys=True))

#after json.dumps() the result is not a dictionary anymore

data={"red":"apple"}

result=json.dumps(data)
print(type(result))
# #will error because it's a string and 
print(result[0]) #change it from a string to whatever this is

#change it back to string
python_object=json.loads(result)
print(python_object)
print(type(python_object))