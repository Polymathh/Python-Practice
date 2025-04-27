expenses = []

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Choose: ")

    if choice == "1":
        item = input("What did you spend on? ")
        amount = float(input("How much? "))
        expenses.append({"item": item, "amount": amount})
    elif choice == "2":
        total = 0
        for expense in expenses:
            print(f"{expense['item']}: ${expense['amount']}")
            total += expense["amount"]
        print(f"Total: ${total}")
    elif choice == "3":
        break
    else:
        print("Invalid choice")
