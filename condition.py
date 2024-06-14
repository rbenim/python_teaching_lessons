#conditions
n = int(input("Number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
 print("n is zero");


#Nested conditions


users = {"ama", "kofi", "yaw", "kila nkuto"}
users.add("Jack Chan")
users.add("kwame")

login_cred = input("Username: ")
password = input("Password: ")

if login_cred in users:
    if password == "1234":  # Assuming the password is "1234" for this example
        print(f"{login_cred} and the password are both correct")
    else:
        print(f"Only {login_cred} is correct but the entered password is wrong")
else:
    print("All credentials are fake")


#Nested conditions

x = 15
y = 20

if x > 10:
    if y > 15:
        print("x is greater than 10 and y is greater than 15")
    else:
        print("x is greater than 10 but y is not greater than 15")
else:
    print("x is not greater than 10")




#logical Operators

x = 5
y = 10

if x < 10 and y > 5:
    print("Both conditions are true")

if x < 10 or y < 5:
    print("At least one of the conditions is true")

if not x > 10:
    print("x is not greater than 10")


