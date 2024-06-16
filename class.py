#Classes in Python are a fundamental part of object-oriented programming (OOP), 
# which allows you to create your own data types and organize your code into reusable and modular
#  pieces. Here's a comprehensive introduction to classes in Python:
#Basic Concepts
#Class: A blueprint for creating objects (a particular data structure).
#Object: An instance of a class.
#Attributes: Variables that belong to an object or class.
#Methods: Functions that belong to an object or class.


#Defining a Class
#To define a class, you use the class keyword followed by the class name and a colon. By convention,
#class names are written in CamelCase.

class Person:
    pass
#Person is the name of my class. so far it has no object(instance) or method

#Creating an Instance (Object) of a Class as person1
person1 = Person()

#You can add attributes and methods to a class to define its behavior and characteristics.
#Initializing Attributes with __init__
#The __init__ method initializes an object's attributes. 
# It is called automatically when an object is created.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def greet(self, hometown):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am from {hometown}")

    def age_calc(self):
        return self.age * 2

# Creating an instance and calling methods
name = input("Name: ")
age = int(input("Your age: "))

person1 = Person(name, age)
person1.greet("Kokofu")  # Output: Hello, my name is [name] and I am [age] years old. I am from Kokofu.
print(person1.age_calc())  # Output: [age * 2]



#Example: Defining a Class with Methods
#Here is a more detailed example to illustrate classes, attributes, and methods:

#creating flight reservation 

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seat(self):
        return self.capacity -len(self.passengers)
    
    def add_passengers(self, name):
        if self.open_seat():
            self.passengers.append(name)
            print(f"Added {name} successfuly")
        else:
            print("No Available seat for {name}.")

flight = Flight(capacity=3)
people = ["Kofi", "Ama", "Yaa", "Kwadwo", "Manu"]
for person in people:
    flight.add_passengers(person)


#House Rent Management
class HouseRent():
    def __init__(self, a_rooms):
        self.a_rooms =a_rooms
        self.tenants = []

    def v_room(self):
        return self.a_rooms - len(self.tenants)
    
    def add_tenants(self, n_tenants):
        if self.v_room():
            self.tenants.append(n_tenants)
            print(f"{n_tenants} has now become our neighbor")
        else:
            print(f"There is no room for {n_tenants}")

rent = HouseRent(a_rooms=3)
applicants = ["manu", "beatrice", "Rose", "Efo", "sandra"]
for new_app in applicants:
    rent.add_tenants(new_app)







