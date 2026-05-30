#Collection Types - holds multiple things - 4 types: 
#Lists -  ordered
#Tuples - immuable, sets, 
#Dictionaries - ordered, mutable, keys can't have multiples/duplicates (can't remember)

#Dictionary
#a key identify where something is, without key you cannot easily find value
#Every student has a locker
lockers = { 
    101: "Books", # key: "value" pair
    102: "Laptop",
    103: "Jacket"
}

#another key:value pair example.  the key helps u identify the value
my_car = {
    "brand":"Hyundai",
    "model":"Elantra",
    "year": 2021
}

#Access a value inside a dictionary
#What year is your car?
print(my_car["year"])

#Use .get method
#Get will check to make sure there is actually something to get.  Print just forces it.
print(my_car.get("price"))
car_brand=my_car.get("brand")
print(car_brand)  #Hyundai
#you can put it in a variable
my_car["brand"] ="Toyota"

#Dictionary values can hold almost anything.  but not the keys
student={
    "name": "Amy:", #string
    "age": 28,    #integer
    "graduated": True, #boolean
    "classes": ["AWS", "DevOps", "Python"] #list - its a list inside a Dictionary!
}

#KEY RULES
#keys must be unique
#Example of not having a unique key - don't do this!
car = {
    "brand": "Ford",
    "brand": "Toyota"
}
print(car.get("brand"))

#KEYS MUST BE IMMUTABLE
#You cannot change keys
car = {
    "year":2021, #good ex
    1: "Ford" #good ex
}

#Key can't start with a list because lists can be changed and Keys are IMMUTABLE

#METHODS
#.keys() - Give labels only
fruits = {
    "red":"apple",
    "green":"pear",
    "purple":"grape",
}
print(fruits.keys())  #outputs the keys

#.values() method - Gives content only, no labels
print(fruits.values())

#.items() method - give content and label key:value pair
print(fruits.items())

#Dictionaries are MUTABLE = changeable
car={
    "brand":"Ford",
    "year":1964
 
}
car["year"]= 2025 #changes exsisting value
print(car)

#add a new value
car["color"]="Pink" #adds a new key:value pair color:pink
print(car) 

#.update()
car.update({
    "owner": "Amy"
})
print(car)

#Checking if key exists
random={
    "Pineapple":"House",
    "Sponge":"Square",
}
if "star" in random:
    print("found")
else: 
    print("not found")
    
    
#REMOVING ITEMS
food = {
    "chicken":"bbq",
    "smoked": False,
    "Hot":"Dog"
}
#.pop() #remove by key
food.pop("Hot")
print(food)

#.popitem() = Remove the last thing inserted
food.popitem()
print(food)

# #del - delete the exact key
# del food["smoked"]
# print(food)

#.clear() - Erase everything but variable still exsists
food.clear()
print(food)

#looping dictionaries
games={
    "Sims":"Fun",
    "Fifa":"Socoer",
    "Madden":"Football",
}
#By default python automatically loops through keys
for thing in games:
    print(thing)
    #the above says the same thing as :
    # for thing in car.keys():
    
for value in games.values():
    print(value)
    
    #.items
    for key, value in games.items():
        print(key, value)
        
    