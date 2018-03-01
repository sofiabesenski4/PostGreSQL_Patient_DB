README.md

The scripts in this folder contain code from pygresql, postgresql, and SQL.

Create_Patient_Test_DB.py creates a "patients" table within the database (which should already be initialized) called "patient_test_db".
insert_dummy_data.py inserts 10 randomly generated patients into the database.



modules used: 
PyGreSQL- used as an interface to allow a python 3 script to utilize both postgresql commands and SQL queries.

PostGreSQL- a Relational Database Management System which has both serverside and clientside functionality.
	The RDBMS relies on the declaritive SQL query language, as well as some C code to manage connections, storage,
	data, etc. basically everything that goes on behind the scenes in a database, as well as the front end interface you can interact with.
	
SQL- the basic building block behind both PostGreSQL and PyGreSQL. It is the "Structured Query Language" which works much different than OO languages.
	Not to be used directly for server management / back end functionality.


Notes:
The date input from python into PostGreSQL needs to be of string format, so remember to typecast it as such. 
