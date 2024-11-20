
''' May need to add some sort of connection to the database '''

def main_menu():
    while True:
        print("\033[H\033[J")
        
        # Main Menu Header
        print("=" * 40)
        print(" Welcome to Stock Brokerage Firm")
        print("=" * 40)
        
        # Menu Options
        print("1. Manage Clients")
        print("2. Manage Accounts")
        print("3. Manage Brokers")
        print("4. Manage Transactions")
        print("5. Manage Trades")
        print("6. Manage Stocks")
        print("7. Manage Branches")
        print("8. Exit")
        print("=" * 40)
        
        # User Input
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            manage_clients()
        elif choice == "2":
            manage_accounts()
        elif choice == "3":
            manage_brokers()
        elif choice == "4":
            manage_transactions()
        elif choice == "5":
            manage_trades()
        elif choice == "6":
            manage_stocks()
        elif choice == "7":
            manage_branches()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Placeholder functions for the submenus
def manage_clients():
    while True:
        print("\nManage Clients")
        print("=" * 40)
        print("1. View All Clients")
        print("2. Add Client")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Clients")
        elif choice == "2":
            add_client()
        elif choice == "3":
            update_client()
        elif choice == "4":
            delete_record("Clients", "Client_ID")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")

#def add_client():

#def update_client():

def manage_accounts():
    while True:
        print("\nManage Accounts")
        print("=" * 40)
        print("1. View All Accounts")
        print("2. Add Account")
        print("3. Update Account")
        print("4. Delete Account")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Accounts")
        elif choice == "2":
            add_account()
        elif choice == "3":
            update_account()
        elif choice == "4":
            delete_record("Accounts", "Acct_Num")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")

#def add_account():

#def update_account():

def manage_brokers():
    while True:
        print("\nManage Brokers")
        print("=" * 40)
        print("1. View All Brokers")
        print("2. Add Brokers")
        print("3. Update Brokers")
        print("4. Delete Brokers")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Broker")
        elif choice == "2":
            add_brokers()
        elif choice == "3":
            update_brokers()
        elif choice == "4":
            delete_record("Broker", "Broker_ID")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")

#def add_brokers():

#def update_brokers():

def manage_transactions():
    while True:
        print("\nManage Transactions")
        print("=" * 40)
        print("1. View All Transactions")
        print("2. Add Transaction")
        print("3. Update Transactions")
        print("4. Delete Transactions")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Transactions")
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            update_transaction()
        elif choice == "4":
            delete_record("Transactions", "Transaction_ID")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")

#def add_transaction():

#def update_transaction():
def manage_trades():
    while True:
        print("\nManage Trades")
        print("=" * 40)
        print("1. View All Trades")
        print("2. Add Trades")
        print("3. Update Trades")
        print("4. Delete Trades")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Trade")
        elif choice == "2":
            add_trade()
        elif choice == "3":
            update_trade()
        elif choice == "4":
            delete_record("Trade", "Trade_ID")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")

#def add_trade():

#def update_trade():
def manage_stocks():
    while True:
        print("\nManage Stocks")
        print("=" * 40)
        print("1. View All Stocks")
        print("2. Add Stocks")
        print("3. Update Stocks")
        print("4. Delete Stocks")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Stocks")
        elif choice == "2":
            add_stocks()
        elif choice == "3":
            update_stocks()
        elif choice == "4":
            delete_record("Stocks", "Stock_ID")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")

#def add_stocks():

#def update_stocks():
def manage_branches():
    while True:
        print("\nManage Branches")
        print("=" * 40)
        print("1. View All Branches")
        print("2. Add Branches")
        print("3. Update Branches")
        print("4. Delete Branches")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Branch")
        elif choice == "2":
            add_branch()
        elif choice == "3":
            update_branch()
        elif choice == "4":
            delete_record("Branch", "Branch_ID")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")

#def add_branch():

#def update_branch():
# Main Execution
if __name__ == "__main__":
    main_menu()
