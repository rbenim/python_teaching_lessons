#Defining a Function
#A function in Python is defined using the def keyword, 
#followed by the function name and parentheses().
# Here is a simple example:
def greet():
    print("Hello, World!")

#Calling a Function
#Once a function is defined, you can call it by using its name followed by parentheses:
greet()


#Function Arguments
#Functions can take arguments, 
# which are values you pass into the function to be used within it.
#Here’s an example with one argument:

# Get the user's name
name = input("Name: ")

# Define the greeting function
def greet(name):
    print(f"Hello, {name}")

# Call the function with the user's name
greet(name)


import datetime
# Getting residential input from the user
town = input("Where do you stay? ")
home_address = input("Residential Address: ")
home_town = input("Where do you come from? ")

# Defining the function to print residential details
def residential(town, home_address, home_town):
    print(f"You're currently staying at {town}, you're from {home_town}, and your residential address is {home_address}")
    print(f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')}")

# Calling the function with the provided inputs
residential(town, home_address, home_town)




#Return Statement
#Functions can also return values using the return statement. 
# Here’s an example:


def add(a, b):
    return a + b
result = add(3, 5)
print(result)




def square(x):
    return x*x
for item in range(10):
    print(f"The square of {item} is {square(item)}")


def addition(x):
    return x + 2

for numbers in range(5):
    print(f"When 2 is added to {numbers} you will get {addition(numbers)}")

results = [addition(numbers) for numbers in range(5)]
print(results)  # This will print the list of results
print(6 in results)  # This will check if 6 is in the results


#Variable-length Arguments
#Python allows you to create functions that accept an arbitrary number of arguments
#  using *args and **kwargs:

#*args for a variable number of positional arguments
#**kwargs for a variable number of keyword arguments
#Here's an example:


#*args
def greet(*names):
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")

#**args
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="Wonderland")


