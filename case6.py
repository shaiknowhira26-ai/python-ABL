
balance = float(input("Enter opening balance: "))

if balance < 0:
    print("Invalid balance")
else:
    while True:
        print("\nD - Deposit")
        print("W - Withdraw")
        print("Q - Quit")

        choice = input("Enter choice: ").upper()

        if choice == "Q":
            break
        elif choice == "D" or choice == "W":
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Enter a positive amount")
            elif choice == "D":
                balance += amount
                print("Deposit successful")
            elif amount <= balance:
                balance -= amount
                print("Withdrawal successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid choice")

    print("Final balance: Rs.", round(balance, 2))
