age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ").lower()

if age >= 18:
    if citizen == "yes":
        print("You are eligible to vote!")
    else:
        print("You must be a citizen to vote.")
else:
    print("You must be 18 or older to vote.")
