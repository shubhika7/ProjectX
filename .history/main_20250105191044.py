import sys
import cs
#from account_operations import create_account, delete_account, view_all_accounts, load_accounts, save_accounts

def create_account(filename='accounts.txt'):
    """
    Prompts the user for account details (number, name, password, balance)
    and appends them as a CSV row to the file specified by filename.
    """

    # Prompt the user for inputs
    account_number = input("Enter account number: ").strip()
    name = input("Enter name: ").strip()
    password = input("Enter password: ").strip()

    # Validate the balance input
    try:
        balance = float(input("Enter initial balance: ").strip())
    except ValueError:
        print("Invalid balance. Please enter a numeric value.")
        return

    # Open the file in append mode and write a new CSV row
    # newline='' helps avoid extra blank lines in Windows environments
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([account_number, name, password, balance])

    print("\nAccount created successfully!")
    
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
            create_account()
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