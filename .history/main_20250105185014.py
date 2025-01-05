import sys
#from account_operations import create_account, delete_account, view_all_accounts, load_accounts, save_accounts

def main():
    accounts = load_accounts()  # Load from JSON/CSV
    while True:
        print("\n=== Bank System ===")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. View All Accounts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account(accounts)
            save_accounts(accounts)
        elif choice == '2':
            delete_account(accounts)
            save_accounts(accounts)
        elif choice == '3':
            view_all_accounts(accounts)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()