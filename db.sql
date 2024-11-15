--Creating OG Database
CREATE DATABASE Brokerage;
USE Brokerage;

-- Clients table
CREATE TABLE Clients (
    Client_ID INT AUTO_INCREMENT PRIMARY KEY,
    Client_Name VARCHAR(100),
    Acct_Num INT,
    DOB DATE,
    Risk_Tolerance VARCHAR(10) with check (Risk_Tolerance in ('High', 'Medium', 'Low')),
    Phone_Number VARCHAR(15),
    Acct_Num INT,
    Foreign Key (Acct_Num) REFERENCES Client_Accounts(Acct_Num)
);

-- Accounts table
CREATE TABLE Accounts (
    Acct_Num INT PRIMARY KEY,
    Acct_Type VARCHAR(15) with check (Acct_Type in ('Checking', 'Savings', 'Investment')),
    Balance DECIMAL(10, 2),
    StatusOf VARCHAR(10) with check (StatusOf in ('Active', 'Inactive', 'Closed')),
    Client_ID INT,
    Foreign Key (Client_ID) REFERENCES Client_Accounts(Client_ID),
    Broker_ID INT,
    Foreign Key (Broker_ID) REFERENCES Broker(Broker_ID)
);

-- Transactions table
CREATE TABLE Transactions (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
    Transaction_Type VARCHAR(10) with check (Transaction_Type in ('Deposit', 'Withdrawal')),
    Transaction_Date DATE NOT NULL,
    Amount DECIMAL(10, 2),
    Acct_Num INT NOT NULL,
    Foreign Key (Acct_Num) REFERENCES Accounts(Acct_Num),
    Client_ID INT,
    Foreign Key (Client_ID) REFERENCES Clients(Client_ID)
);

-- Brokers table
CREATE TABLE Broker (
    Broker_ID INT AUTO_INCREMENT PRIMARY KEY,
    Broker_Name VARCHAR(30),
    License_Num VARCHAR(20),
    Experience_LVL INT NOT NULL CHECK (Experience_LVL BETWEEN 1 AND 4),
    Branch_ID INT,
    Foreign Key (Branch_ID) REFERENCES Branch(Branch_ID)
);

-- Trades table
CREATE TABLE Trade (
    Trade_ID INT AUTO_INCREMENT PRIMARY KEY,
    Trade_Type VARCHAR(20) with check (Trade_Type in ('Buy', 'Sell')),
    Trade_Date DATE,
    Quantity INT,
    Price_Per DECIMAL(10, 2),
    Broker_ID INT,
    Foreign Key (Broker_ID) REFERENCES Broker(Broker_ID),
    Acct_Num INT,
    Foreign Key (Acct_Num) REFERENCES Accounts(Acct_Num),
    Stock_ID INT,
    Foreign Key (Stock_ID) REFERENCES Stocks(Stock_ID)
);

-- Stocks table
CREATE TABLE Stocks (
    Stock_ID INT AUTO_INCREMENT PRIMARY KEY,
    Ticker VARCHAR(10),
    ReturnValue DECIMAL(5, 2),
    Industry VARCHAR(50),
    Current_Price DECIMAL(10, 2)
);

-- Branch table
CREATE TABLE Branch (
    Branch_ID INT AUTO_INCREMENT PRIMARY KEY,
    LocationOf VARCHAR(100),
    Manager VARCHAR(20),
    Manager_ID INT,
    Contact VARCHAR(15)
);

-- Junction Tables for many-to-many relationships
-- Client_Accounts Junction Table
CREATE TABLE Client_Accounts (
    Client_ID INT,
    Acct_Num INT,
    Primary Key (Client_ID, Acct_Num),
    Foreign Key (Client_ID) REFERENCES Clients(Client_ID),
    Foreign Key (Acct_Num) REFERENCES Accounts(Acct_Num)
);



