INSTRUCTIONS FOR SETTING UP AND USING OUR DATABASE:

Setting up:
The database is made for MySQL, so having a working version of MySQL on your device is necessary for setup. The CLI uses mySQL-connector which is installed with the command: pip install mysql-connector-python. Remember the username and password you use for setting up the database, because it will be necessary for using the CLI later. Once in whatever version of MySQL you choose to use, run db.sql, which will set up the initial database and schemas.
Next, run InsertData.sql. This will insert all of the data for testing purposes into the database. Now your database should be initialized for running the test queries.


Setting Up the CLI:

All of the test queries can also be run in whatever version of MySQL that you use. These test queries can be found in the essay.
For setting up the CLI version, open mainmenu.py. In mainmenu.py, set your username equal to whatever username you used earlier and your password to whatever you used for your password earlier. You may also need to modify the value of host if you are not using localhost. However the database value should always remain 'brokerage'. 
After this, you should be able to run mainmenu.py and have it properly connect to your local version of the database. From here you can test out the CLI equivalents of the test queries.

Test Query and CLI Testing:
NOTE: All of the CLI equivalent's instructions assume that you are at the home page of the menu. For the purpose of testing, please return to the main menu after each test. 

1) Goal: Show all of the data from the various brokerage branches.
  SQL Query: select * from branch;
  CLI Equivalent: Enter 7 to see the manage branches menu, then enter 1 to see all branch data

2) Goal: Modify existing data from branch 104 to update the location to Dallas instead of Houston.
  SQL Query: update branch set LocationOf = "Dallas" where Branch_ID = 104;
  CLI Equivalent: Enter 7 to manage branches, enter 3 to update branches, enter 104 for the Branch ID to update, enter Dallas for the modified location and skip through the rest of the prompts. 

3) Goal: Add a new broker to the broker table.
  SQL Query: insert into broker(Broker_ID, Broker_Name, License_Num, Experience_LVL, Branch_ID)
             values (51, "Nathaniel", "32E6FKL9", 4, 103);
  CLI Equivalent: Enter 3 to manage brokers, enter 2 to add brokers, when prompted enter a broker_ID of 51, Broker Name of Nathaniel, License Number of 32E6FKL9, Experience Level fo 4, and Branch ID of 103. This should successfully insert your new broker into the database. 

4) Goal: Show all brokers that are currently in the broker table (This will show where we added Nathaniel)
  SQL Query: select * from broker;
  CLI Equivalent: Enter 3 to manage brokers, enter 1 to see all data in the brokers table

5) Goal: Delete the new broker that has just been added.
  SQL Query: delete from broker where Broker_ID = 51;
  CLI Equivalent: Enter 3 to manage brokers, enter 4 to delete brokers, and enter a broker ID of 51 to delete Nathaniel from the table. 
