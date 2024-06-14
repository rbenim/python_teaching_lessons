#DATA STRUCTURE IN PYTHON.............................


#difference between tuple and list
#list is enclosed in brackets [] and  turples in square brackets ()
# list can be modifield but not turples. examples

#list
my_list = [1, 2, 3, 4, 5, "and", 6]

#sort list
sort_list = my_list.sort

#modification
my_list[2] = "two"
print(my_list)

#turple. this turple can not be modified
my_turple = (1, 2, 3, 4, 5, "and", 6)
print(my_turple)




#range
my_range = range(5, 20)

#slice
selected_range = my_range[2:6]
preffered_number = my_range[8] *2
concate_items = (f"{selected_range}, these two numbers were selected the 3rd and 6th positions a range between 5 and 20")
print(concate_items)
print(selected_range)
print(preffered_number)
for item in my_range:
   print(item)

#length   
range_length = len(my_range)
print(f"Range length is {range_length}")



#Creating a Set
#You can create a set using curly braces {} or the set() function.
my_set = {"Kwaku", "man", "yaw", "Crinton", "Obama", "Trump"}

#addition of members
my_set.add("Richard")

#removal of members
my_set.remove("man")

print(my_set)  # This will print the updated set

#Set operations

set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a | set_b  # {1, 2, 3, 4, 5}
union_set = set_a.union(set_b)  # {1, 2, 3, 4, 5}

print(f"the union set of a and b is: {union_set}")

# Intersection
intersection_set = set_a & set_b  # {3}
intersection_set = set_a.intersection(set_b)  # {3}

print(f"the intersection set of a and b is: {intersection_set}")


# Difference
difference_set = set_a - set_b  # {1, 2}
difference_set = set_a.difference(set_b)  # {1, 2}

print(f"the difference in set of a and b is: {difference_set}")


# Symmetric Difference
sym_diff_set = set_a ^ set_b  # {1, 2, 4, 5}
sym_diff_set = set_a.symmetric_difference(set_b)  # {1, 2, 4, 5}

print(f"the symmetric difference in set of a and b is: {sym_diff_set}")

#membership test
print(3 in union_set)
print(4 in intersection_set)


