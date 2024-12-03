
#THIS IS JUST AN EXAMPLE ONLY THING THAT NEEDS TO BE DONE ON THIS END
import mysql.connector
from mysql.connector import Error

def get_connection():
    """Connect to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  
            password="password",  
            database="brokerage"  
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None


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
            print("Thank you for your service. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Function to execute SELECT queries
def view_records(table_name):
    """View all records from a table."""
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            print(f"\n{table_name} Records:")
            for row in rows:
                print(row)
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Function to delete a record
def delete_record(table_name, primary_key):
    """Delete a record from the specified table."""
    record_id = input(f"Enter {primary_key} of the record to delete: ")
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(f"DELETE FROM {table_name} WHERE {primary_key} = %s", (record_id,))
            connection.commit()
            print(f"Record with {primary_key} = {record_id} deleted successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

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

def add_client():
    name = input("Enter Client Name: ")
    acct_num = input("Enter Account Number: ")
    dob = input("Enter Date of Birth (MM-DD-YYYY): ")
    risk_tolerance = input("Enter Risk Tolerance (Low, Medium, High): ")
    phone_number = input("Enter Phone Number: ")

    #need to add something to connect it to the database
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Clients (Client_Name, Acct_Num, DOB, Risk_Tolerance, Phone_Number)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (name, acct_num, dob, risk_tolerance, phone_number)
            )
            connection.commit()
            print("Client added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def update_client():
    client_id = input("Enter The Client ID to Update: ")
    name = input("Enter the Client Name (press enter to skip): ")
    phone_number = input("Enter the new Phone Number (press enter to skip): ")

     #need to add something to connect it to the database
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            updates = []
            params = []
            if name:
                updates.append("Client_Name = %s")
                params.append(name)
            if phone_number:
                updates.append("Phone_Number = %s")
                params.append(phone_number)
            params.append(client_id)
            if updates:
                query = f"UPDATE Clients SET {', '.join(updates)} WHERE Client_ID = %s"
                cursor.execute(query, tuple(params))
                connection.commit()
                print("Client updated successfully.")
            else:
                print("No updates provided.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

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
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Accounts (Acct_Type, Balance, StatusOf, Client_ID, Broker_ID)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (acct_type, balance, status, client_id, broker_id)
            )
            connection.commit()
            print("Account added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def update_account():
    acct_num = input("Enter The Account Number to Update: ")
    acct_type = input("Enter the Account Type (press enter to skip): ")
    balace = input("Enter the new Balance (press enter to skip): ")
    status = input("Enter the new Status (press enter to skip): ")

     #need to add something to connect it to the database
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            updates = []
            params = []
            if acct_type:
                updates.append("Acct_Type = %s")
                params.append(acct_type)
            if balance:
                updates.append("Balance = %s")
                params.append(balance)
            if status:
                updates.append("StatusOf = %s")
                params.append(status)
            params.append(acct_num)
            if updates:
                query = f"UPDATE Accounts SET {', '.join(updates)} WHERE Acct_Num = %s"
                cursor.execute(query, tuple(params))
                connection.commit()
                print("Account updated successfully.")
            else:
                print("No updates provided.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

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
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Broker (Broker_Name, License_Num, Experience_LVL, Branch_ID)
                VALUES (%s, %s, %s, %s)
                """,
                (name, license_num, experience, branch_id)
            )
            connection.commit()
            print("Broker added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
            
def update_brokers():
    broker_id = input("Enter The Broker ID to Update: ")
    name = input("Enter the Broker Name (press enter to skip): ")
    license_num= input("Enter the new License Number (press enter to skip): ")
    experience = input("Enter the new Experience Level (press enter to skip): ")
    branch_id = input("Enter the new Branch ID (press enter to skip): ")
     #need to add something to connect it to the database
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            updates = []
            params = []
            if name:
                updates.append("Broker_Name = %s")
                params.append(name)
            if license_num:
                updates.append("License_Num = %s")
                params.append(license_num)
            if experience:
                updates.append("Experience_LVL = %s")
                params.append(experience)
            if branch_id:
                updates.append("Branch_ID = %s")
                params.append(branch_id)
            params.append(broker_id)
            if updates:
                query = f"UPDATE Broker SET {', '.join(updates)} WHERE Broker_ID = %s"
                cursor.execute(query, tuple(params))
                connection.commit()
                print("Broker updated successfully.")
            else:
                print("No updates provided.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

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
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Transactions (Transaction_Type, Transaction_Date, Amount, Acct_Num, Client_ID)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (transaction_type, transaction_date, amount, acct_num, client_id)
            )
            connection.commit()
            print("Transaction added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

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
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Trade (Trade_Type, Trade_Date, Quantity, Price_Per, Broker_ID, Acct_Num, Stock_ID)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (trade_type, trade_date, quantity, price_per, broker_id, acct_num, stock_id)
            )
            connection.commit()
            print("Trade added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
            
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
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Stocks (Ticker, ReturnValue, Industry, Current_Price)
                VALUES (%s, %s, %s, %s)
                """,
                (ticker, return_value, industry, current_price)
            )
            connection.commit()
            print("Stock added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

def update_stocks():
    client_id = input("Enter The Client ID to Update: ")
    name = input("Enter the new Client Name (press enter to skip): ")
    phone_number = input("Enter the new Phone Number (press enter to skip): ")

     #need to add something to connect it to the database
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            updates = []
            params = []
            if ticker:
                updates.append("Ticker = %s")
                params.append(ticker)
            if current_price:
                updates.append("Current_Price = %s")
                params.append(current_price)
            params.append(stock_id)
            if updates:
                query = f"UPDATE Stocks SET {', '.join(updates)} WHERE Stock_ID = %s"
                cursor.execute(query, tuple(params))
                connection.commit()
                print("Stock updated successfully.")
            else:
                print("No updates provided.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
            
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
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(
                """
                INSERT INTO Branch (LocationOf, Manager, Manager_ID, Contact)
                VALUES (%s, %s, %s, %s)
                """,
                (location, manager, manager_id, contact)
            )
            connection.commit()
            print("Branch added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()
            
def update_branch():
    branch_id = input("Enter Branch ID to update: ")
    location = input("Enter the new Location (press enter to skip): ")
    manager = input("Enter the new Manager Name (press enter to skip): ")
    contact = input("Enter the new Contact Number (press enter to skip): ")
     #need to add something to connect it to the database
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            updates = []
            params = []
            if location:
                updates.append("LocationOf = %s")
                params.append(location)
            if manager:
                updates.append("Manager = %s")
                params.append(manager)
            if contact:
                updates.append("Contact = %s")
                params.append(contact)
            params.append(branch_id)
            if updates:
                query = f"UPDATE Branch SET {', '.join(updates)} WHERE Branch_ID = %s"
                cursor.execute(query, tuple(params))
                connection.commit()
                print("Branch updated successfully.")
            else:
                print("No updates provided.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            connection.close()

# Main Execution
if __name__ == "__main__":
    main_menu()
