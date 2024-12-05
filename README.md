INSTRUCTIONS FOR SETTING UP AND USING OUR DATABASE:

Setting up:
The database is made for MySQL, so having a working version of MySQL on your device is necessary for setup. The CLI uses mySQL-connector for the connection between python and mysql, which is installed with the command: pip install mysql-connector-python. Remember the username and password you use for setting up the database, because it will be necessary for using the CLI later. Once in whatever version of MySQL you choose to use, run db.sql, which will set up the initial database and schemas.
Next, run InsertData.sql. This will insert all of the data for testing purposes into the database. Now your database should be initialized for running the test queries.


Setting Up the CLI:

All of the test queries can also be run in whatever version of MySQL that you use. These test queries can be found in the essay.
For setting up the CLI version, open mainmenu.py. In mainmenu.py, set your username equal to whatever username you used earlier and your password to whatever you used for your password earlier. You may also need to modify the value of host if you are not using localhost. However the database value should always remain 'brokerage'. 
After this, you should be able to run mainmenu.py and have it properly connect to your local version of the database. From here you can test out the CLI equivalents of the test queries.

Test Query and CLI Testing:

1) 
2)
3)
4)
5)
