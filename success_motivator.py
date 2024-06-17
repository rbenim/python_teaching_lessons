success = "Welcome to the Team success's success hunt program. Answer the following questions."
answers = "Your answer is yes/no"

hunger = input("Are you hungry for success? (yes/no): ")

if hunger == "yes":
    sacrifice = input("Are you willing to sacrifice? (yes/no): ")
    if sacrifice == "yes":
        print("Sacrificing temporary pleasure for what is good for the future is a prerequisite for success.")
        print("Avoid unnecessary engagements, distractions, and time-wasting activities.")
        cred = input("enter your name: ")
        phone= int(input("Your Phone no: "))
        print(f"Congratulation {cred}, You're Now Welcome To Rich's Successful Club")

    elif sacrifice == "no":
        print("Jack k) fie k)da.")
    else:
        print("You're not serious. Masa, go and sleep.")
elif hunger == "no":
    print("You're not serious. Go home.")
else:
    print("You're unstable. Masa, go and sleep.")
