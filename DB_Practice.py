#DB_Practice.py
"""
Created Feb 27th 2018

All learning notes/meta notes are written in triple quoted comments, while hash comments are talking about the next line specifically

NOTES:

Initially, to run this script, you have to be logged into a user on the linux OS which is recognized
by postgresql as a "role".
ie: on my "green" laptop, you can be logged in as teb8_postgres, and try to access the 'tester' database.

DB class:
This class is a child of the lower level Connection class, which represents the connection to a database



DB wrapper object:

access the primary key of a table by the command "db.pkey(<tablename>)"

PyGreSQL Commands:



<ConnectionIdentifier>.query():
You can execute queries by using the db.query('<write query>') method, but should mainly be reserved for select statements
It is also possible to execute any other operations using this method, since you can hardcore your sql queries into here,
but it is not recommended, since there are pygresql methods which you can use in a more clean fashion

<ConnectionIdentifier>.insert():
You can insert into a table using the db.insert(<table name>, <atrribute1>=<value>, <attribute2>=<value>, ....)
It is computationally more efficient to use the inserttable method of a DB object when inserting multiple rows to a table
To do this, you must have a list of tuples, covered next.

<ConnectionIdentifier>.inserttable():



"""


#importing the DB wrapper class from pygresql
from pg import DB
import datetime
#accessing the database 'tester', assuming you are logged in as teb8_postgres or postgres, which are authorized to access the tester db
db = DB(dbname = "tester")
#printing all the names of the tables in this database
print(db.get_tables())
table_names = db.get_tables()

print("socket number: ",db.fileno())


#the following query added a date attribute to the table fridge_contents, who's default value is the date when the row was added to the table
#db.query("ALTER TABLE {} ADD COLUMN date DATE NOT NULL DEFAULT CURRENT_DATE ".format(table_names[1]))


"""
The following queries changed the primary key of fridge_contents to the ingredients attribute and removed the food_id attribute
"""
#print(db.query("ALTER TABLE fridge_contents DROP CONSTRAINT fridge_contents_pkey;"))
#print(db.query("ALTER TABLE fridge_contents ADD PRIMARY KEY (ingredients);"))


"""
The following query will try to insert a table into the fridge_contents table
"""
print(datetime.date.today())

#insertable_list = [(5,"dairy","milk",3,65,dt.datetime.now()[:3].join("-")),(6,"wheat and carbs","bread",2,200,dt.datetime.now()[:3].join("-")),(7,"fruits and vegetables", "strawberry",14,25,dt.datetime.now()[:3].join("-")),(8,"dairy","cheese",10,430,dt.datetime.now()[:3].join("-"))]
#print(db.inserttable("fridge_contents", insertable_list))

#this will display information about all the tables contained in this database
for table in db.get_tables():
	print("\nDisplaying information corresponding to the {} table:".format(table))
	#printing attribute names and types in a list of tuples
	print("Attributes/columns contained: ",db.get_attnames(table))
	#checking permissions of the current user to see if insert commands can be completed
	print("Able to perform '{}' operations on the '{}' table? ".format('insert', table),db.has_table_privilege(table,'insert'))
	print(db.query("""select * from {};""".format(table)))
	print("The primary key from this table is: ", db.pkey(table))
	
"""



"""
#following query will display the cost (in cents) to complete the brocomushy recipe, considering the required units and price per unit of each ingredients
print(db.query("SELECT SUM(required_units * cents_per_unit) as Cost_Per_Recipe FROM {} inner join {} on fridge_contents.{}=brocomushy_recipe.{} ;".format(table_names[0],
																					table_names[1], db.pkey(table_names[1]), db.pkey(table_names[0]))))







