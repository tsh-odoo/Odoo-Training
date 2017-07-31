For CRUD application using Python Backend and PostgreSQL Database

1) Purpose: Create Table in your existing Database or create new Database(for this do google postgresql create user setuping

Command: CREATE TABLE registration (first_name varchar, last_name varchar);

2) Purpose: Insert Data into this registration table

Command: INSERT INTO registration VALUES ('Tejas', 'Shahu');

So here my table is ready to display existing data into html page.

3) Main Logic in server.py file - what you want to do? Here we want to make crud (Create,Read,Update,Delete) operation:

Some postgresql queries for crud operation

Update Query(should be execute on edit button click): 

Retrieve Data Query(should be executed while page loading first time): 
SELECT * FROM registration;

Insert Query(should be executed on create button click): 
INSERT INTO registration VALUES ('Tejas', 'Shahu');