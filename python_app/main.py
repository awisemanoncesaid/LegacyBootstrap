from data import AccountData
from operations import AccountOperations

def main():
    account = AccountData()
    ops = AccountOperations(account)

    while True:
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print(f"Current balance: {account.get_balance():.2f}")
        elif choice == "2":
            try:
                amount = float(input("Enter amount to credit: "))
                ops.credit(amount)
                print(f"Amount credited. New balance: {account.get_balance():.2f}")
            except ValueError:
                print("Invalid amount.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to debit: "))
                if ops.debit(amount):
                    print(f"Amount debited. New balance: {account.get_balance():.2f}")
                else:
                    print("Insufficient funds for this debit.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
