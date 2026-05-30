# May 18, 2026
def make_burger():
    print("Burger ready!") #McDs shows you your order on teh screen but there's no actual food 
food = make_burger()
print(food)

#print just shows the output, it doesn't give a value.  
#return actually holds a value to pass

#RETURN function
#1st job is Return ends the function immediately
#2 Sends a value back to caller
#McDonalds - when you actually get your food in your hand to hold it, eat it or share it
def make_burger():
    return "Burger"
food = make_burger()
print(food)

def add(x,y):
    return x+y #python sees x+y and gets 8
answer = add(3,5) #answer holds 8 (a real value, unlike print)
print(answer)

def add_print(x,y):
    print(x+y)
result = add_print(3,5)
print(result)
#if you don't include a Return then python sends "none"
#print() - function -> display result -> then gone forever (display only)
#return - function -> return value -> save/use later

#Return works with everything - int, float, string, numbers..etc.

#example with integer
def age():
    return 28
print(age())

#example with strings
def greet():
    return "Hello, Amy!"
print(greet())

#example with list
def lunch():
    return ["pizza", "apple", "juice"]
meal = lunch()
print(meal)

#example with dictionary
def student():
    return{
        "name":"Amy",
        "grade": 100,
    }
    info=student()
    print(info["name"])
    
#Explicit Return - You tell Python exactly what to send back. You can use it for anything from there.  With Return, you actually get a value (Mcds) and u can do whatever with it.
#Implicit Return(none) - You don't tell Python exactly what to send back

#Return Immediately Stops everything
#once Python hits return the function is OVER, Dead, KAPOOT
def example():
    print("Start")
    return 5
    print("End")
example()

#Can have an empty return
def stop_here():
    print("Hello")
    return
    print("Bye")
stop_here() #function call to send the value
#you only got Hello bcuz at return the function stopped.

#empty return - stop now and send nothing back
def stop_here():
    print("Hello")
    return
    print("Bye")
example = stop_here()
print(example) #function call to send the value
stop_here()

def outer(name): #this returns hello amy
    def inner(): #inner uses the peramenter name
        return f"Hello {name}"
    return inner()
message = outer("Amy")
print(message)


