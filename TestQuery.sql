select * from branch;
--shows all data in the branch table

update branch set LocationOf = "Dallas" where Branch_ID = 104;
--Changes the location of branch 104 from Houston to Dallas

insert into broker(Broker_ID, Broker_Name, License_Num, Experience_LVL, Branch_ID)
values (51, "Nathaniel", "32E6FKL9", 4, 103);
--Add a new broker to the broker table

select * from broker;
--Show all data from broker table to confirm new broker has been added

delete from broker where Broker_ID = 51;
--Delete the newly added broker from the broker table
