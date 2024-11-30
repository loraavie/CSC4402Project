import mysql.connector
def get_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "username",
        password = "password",
        database = "brokerage"
    )
    if connection.is_connected():
        print("Connected to Database")
    else: print("Connection Failed. Please check credentials provided.")
    cursor = connection.cursor()
    return connection, cursor


def main_menu():
    while True:
        #commented out bc it throws error on my machine
        #print("\033[H\033[J")
        
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
            print("Thank you for your patronage. Goodbye!")
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
            delete_record()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please Try Again.")
def view_records(table):
    # SQL SELECT Query
    query = "SELECT * FROM clients"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

def add_client():
    client_ID = input("Enter Client ID: ")
    name = input("Enter Client Name: ")
    acct_num = input("Enter Account Number: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    risk_tolerance = input("Enter Risk Tolerance (Low, Medium, High): ")
    phone_number = input("Enter Phone Number: ")

    query = "INSERT INTO clients(client_id, client_name, Account_Number, DOB, Risk_Tolerance, Phone_Number) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (client_ID, name, acct_num, dob, risk_tolerance, phone_number)
    cursor.execute(query, values)
    #need to add something to connect it to the database

def update_client():
    client_id = input("Enter The Client ID to Update: ")
    num = input("What would you like to modify about this client's data? (Name, DOB, Risk Tolerance, Phone Number): \n(1) Name\n(2) DOB\n(3) Risk Tolerance\n(4) Phone Number\n")
    if(num == "1"):
        name = input("Enter the new Client Name: ")
        query = "UPDATE clients SET client_name = %s WHERE client_id = %s"
        values = (name, client_id)
        cursor.execute(query, values)
    elif(num == "2"):
        dob = input("Enter the new Date of Birth: ")
        query = "UPDATE clients SET DOB = %s WHERE client_id = %s"
        values = (dob, client_id)
        cursor.execute(query, values)
    elif(num == "3"):
        risk_tolerance = input("Enter the new Risk Tolerance: ")
        query = "UPDATE clients SET Risk_Tolerance = %s WHERE client_id = %s"
        values = (risk_tolerance, client_id)
        cursor.execute(query, values)
    elif(num == "4"):
        phone_number = input("Enter the new Phone Number: ")
        query = "UPDATE clients SET Phone_Number = %s WHERE client_id = %s"
        values = (phone_number, client_id)
        cursor.execute(query, values)
    else:
        print("Invalid choice. Please Try Again.")
def delete_record():
    record_id = input(f"Enter the Client_ID to delete from clients: ")
    query = f"DELETE FROM clients WHERE Client_ID = %s"
    values = (record_id,)
    cursor.execute(query, values)


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

def add_account():
    acct_type = input("Enter Account Type (Checkings, Savings, etc.): ")
    balace = input("Enter Balance: ")
    status = input("Enter Status (Active, Inactive, Closed): ")
    client_id = input("Enter Client ID: ")
    broker_id = input("Enter Broker ID: ")

    #need to add something to connect it to the database

def update_account():
    acct_num = input("Enter The Account Number to Update: ")
    acct_type = input("Enter the Account Type (press enter to skip): ")
    balace = input("Enter the new Balance (press enter to skip): ")
    status = input("Enter the new Status (press enter to skip): ")

     #need to add something to connect it to the database

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

def add_brokers():
    name = input("Enter Broker Name: ")
    license_num = input("Enter The License Number: ")
    experience = input("Enter Experience Level (1-4): ")
    branch_id = input("Enter Branch ID: ")

    #need to add something to connect it to the database

def update_brokers():
    broker_id = input("Enter The Broker ID to Update: ")
    name = input("Enter the Broker Name (press enter to skip): ")
    license_num= input("Enter the new License Number (press enter to skip): ")
    experience = input("Enter the new Experience Level (press enter to skip): ")
    branch_id = input("Enter the new Branch ID (press enter to skip): ")
     #need to add something to connect it to the database

def manage_transactions():
    while True:
        print("\nManage Transactions")
        print("=" * 40)
        print("1. View All Transactions")
        print("2. Add Transaction")
        print("3. Delete Transactions")
        print("4. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Transactions")
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            delete_record("Transactions", "Transaction_ID")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please Try Again.")

def add_transaction():
    transaction_type = input("Enter Transaction Type (Deposit, Withdrawl): ")
    transaction_date = input("Enter Transaction Date (MM-DD-YYYY): ")
    amount = input("Enter Amount: ")
    acct_num = input("Enter Account Number: ")
    client_id = input("Enter Client ID: ")

    #need to add something to connect it to the database

def manage_trades():
    while True:
        print("\nManage Trades")
        print("=" * 40)
        print("1. View All Trades")
        print("2. Add Trades")
        print("3. Delete Trades")
        print("4. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_records("Trade")
        elif choice == "2":
            add_trade()
        elif choice == "3":
            delete_record("Trade", "Trade_ID")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please Try Again.")

def add_trade():
    trade_type = input("Enter Trade Type (Buy/Sell): ")
    trade_date = input("Enter Trade Date (YYYY-MM-DD): ")
    quantity = input("Enter Quantity: ")
    price_per = input("Enter Price Per Unit: ")
    broker_id = input("Enter Broker ID: ")
    acct_num = input("Enter Account Number: ")
    stock_id = input("Enter Stock ID: ")

    #need to add something to connect it to the database

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

def add_stocks():
    name = input("Enter Client Name: ")
    acct_num = input("Enter Account Number: ")
    dob = input("Enter Date of Birth (MM-DD-YYYY): ")
    risk_tolerance = input("Enter Risk Tolerance (Low, Medium, High): ")
    phone_number = input("Enter Phone Number: ")

    #need to add something to connect it to the database

def update_stocks():
    client_id = input("Enter The Client ID to Update: ")
    name = input("Enter the new Client Name (press enter to skip): ")
    phone_number = input("Enter the new Phone Number (press enter to skip): ")

     #need to add something to connect it to the database

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

def add_branch():
    location = input("Enter Branch Location: ")
    manager = input("Enter Manager Name: ")
    manager_id = input("Enter Manager ID: ")
    contact = input("Enter Contact Number: ")

    #need to add something to connect it to the database

def update_branch():
    branch_id = input("Enter Branch ID to update: ")
    location = input("Enter the new Location (press enter to skip): ")
    manager = input("Enter the new Manager Name (press enter to skip): ")
    contact = input("Enter the new Contact Number (press enter to skip): ")
     #need to add something to connect it to the database

# Main Execution
if __name__ == "__main__":
    connection, cursor = get_connection()
    main_menu()
