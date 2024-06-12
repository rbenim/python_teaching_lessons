
#using formatted string
name = input("Name: ")
print(f"Hello, {name}");

#conditions
n = int(input("Number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
 print("n is zero");

 #Sequence. selecting a sprcific letter in a
names = input("Names: ")
print(names[2])

plist = ["many", "Kofi", "Yaw"]
print(plist[1])

# Creating a string
my_string = "Hello, World!"

# Accessing elements
first_char = my_string[0]   # 'H'
last_char = my_string[-1]   # '!'

# Slicing
substring = my_string[0:5]  # 'Hello'

# Iterating
for char in my_string:
    print(char)

#range
my_range = range(5, 20)

selected_range = my_range[2:6]
preffered_number = my_range[8] *2
concate_items = (f"{selected_range}, these two numbers were selected the 3rd and 6th positions a range between 5 and 20")
print(concate_items)
print(selected_range)
print(preffered_number)
for item in my_range:
   print(item)
