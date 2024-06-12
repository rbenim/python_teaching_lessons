#conditions
n = int(input("Number: "))
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
 print("n is zero");


users = {"ama" , "kofi", "yaw" , "kila nkuto"}
users.add("Jack Chan")
users.add("kwame")
login_cred = input("Username:")

if login_cred in users:
   print(f"user's credential is legit this is the list of {users}")
else:
   print("user is fake")
