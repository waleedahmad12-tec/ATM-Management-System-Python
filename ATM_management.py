balance = 50000
pin = "1234"
transactions = []

user_pin = input("Enter ATM PIN: ")

if user_pin == pin:

    print("\nLogin Successful!")

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Enter Choice: ")

        # Check Balance
        if choice == "1":
            print("Current Balance:", balance)

        # Deposit
        elif choice == "2":

            amount = float(input("Enter Deposit Amount: "))

            balance += amount

            transactions.append(
                f"Deposited Rs.{amount}"
            )

            print("Amount Deposited Successfully!")

        # Withdraw
        elif choice == "3":

            amount = float(input("Enter Withdraw Amount: "))

            if amount <= balance:

                balance -= amount

                transactions.append(
                    f"Withdraw Rs.{amount}"
                )

                print("Withdrawal Successful!")

            else:
                print("Insufficient Balance!")

        # Transaction History
        elif choice == "4":

            if len(transactions) == 0:
                print("No Transactions Yet")

            else:

                print("\nTransaction History:")

                for transaction in transactions:
                    print("-", transaction)

        # Exit
        elif choice == "5":

            print("Thank You For Using ATM")
            break

        else:
            print("Invalid Choice")

else:
    print("Incorrect PIN")