import sys
#from account_operations import create_account, delete_account, view_all_accounts, load_accounts, save_accounts

def create_account(accounts):
    name = input("Enter account holder name: ")
    account_number = input("Enter a unique account number: ")
    # Check if account_number already exists
    if any(acc["account_number"] == account_number for acc in accounts):
        print("Error: Account number already exists!")
        return

    try:
        initial_balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance. Account not created.")
        return

    new_account = {
        "account_number": account_number,
        "name": name,
        "balance": initial_balance
    }
    accounts.append(new_account)
    print(f"Account {account_number} created successfully!")
def main():
 #   accounts = load_accounts()  # Load from JSON/CSV
    while True:
        print("\n=== Bank System ===")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account(accounts)
        #     save_accounts(accounts)
        # elif choice == '2':
        #     delete_account(accounts)
        #     save_accounts(accounts)
        # elif choice == '3':
        #     view_all_accounts(accounts)
        # elif choice == '4':
        #     print("Exiting...")
        #     break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()