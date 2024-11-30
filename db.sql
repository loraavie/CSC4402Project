CREATE DATABASE Brokerage;
USE Brokerage;

-- Branch table
CREATE TABLE Branch (
    Branch_ID INT AUTO_INCREMENT PRIMARY KEY,
    LocationOf VARCHAR(100),
    Manager VARCHAR(20),
    Manager_ID INT,
    Contact VARCHAR(15)
);

-- Broker table
CREATE TABLE Broker (
    Broker_ID INT AUTO_INCREMENT PRIMARY KEY,
    Broker_Name VARCHAR(30),
    License_Num VARCHAR(20),
    Experience_LVL INT NOT NULL,
    Branch_ID INT,
    FOREIGN KEY (Branch_ID) REFERENCES Branch(Branch_ID)
);

-- Stocks table
CREATE TABLE Stocks (
    Stock_ID INT AUTO_INCREMENT PRIMARY KEY,
    Ticker VARCHAR(10),
    ReturnValue DECIMAL(5, 2),
    Industry VARCHAR(50),
    Current_Price DECIMAL(10, 2)
);
-- Clients table
CREATE TABLE Clients (
    Client_ID INT AUTO_INCREMENT PRIMARY KEY,
    Client_Name VARCHAR(100),
    Account_Number int,
    DOB DATE,
    Risk_Tolerance VARCHAR(10),
    Phone_Number VARCHAR(15)
);
-- Accounts table
CREATE TABLE Accounts (
    Acct_Num INT PRIMARY KEY,
    Acct_Type VARCHAR(15),
    Balance DECIMAL(10, 2),
    StatusOf VARCHAR(10),
    Client_ID INT,
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID),
    Broker_ID INT,
    FOREIGN KEY (Broker_ID) REFERENCES Broker(Broker_ID)
);

-- Client_Accounts table
CREATE TABLE Client_Accounts (
    Client_ID INT,
    Acct_Num INT,
    PRIMARY KEY (Client_ID, Acct_Num),
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID),
    FOREIGN KEY (Acct_Num) REFERENCES Accounts(Acct_Num)
);

-- Transactions table
CREATE TABLE Transactions (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
    Transaction_Type VARCHAR(10),
    Transaction_Date DATE NOT NULL,
    Amount DECIMAL(10, 2),
    Acct_Num INT NOT NULL,
    FOREIGN KEY (Acct_Num) REFERENCES Accounts(Acct_Num)
);

-- Trade table
CREATE TABLE Trade (
    Trade_ID INT AUTO_INCREMENT PRIMARY KEY,
    Trade_Type ENUM('Buy', 'Sell'),
    Trade_Date DATE,
    Quantity INT,
    Price_Per DECIMAL(10, 2),
    Broker_ID INT,
    FOREIGN KEY (Broker_ID) REFERENCES Broker(Broker_ID),
    Acct_Num INT,
    FOREIGN KEY (Acct_Num) REFERENCES Accounts(Acct_Num),
    Stock_ID INT,
    FOREIGN KEY (Stock_ID) REFERENCES Stocks(Stock_ID)
);
