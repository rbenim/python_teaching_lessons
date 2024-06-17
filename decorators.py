#Basic Concept of Decorators
# A decorator is a function that takes another function as an argument, 
# adds some kind of functionality, and returns a new function.

# Syntax
# The @decorator syntax is a shorthand for applying a decorator to a function. 
# Here’s a simple example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()


#Another try

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

print(add(5, 3))
