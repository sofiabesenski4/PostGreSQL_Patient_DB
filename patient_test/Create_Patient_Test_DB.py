#Create_Patient_Test_DB.py
"""

This script should be run to initialize a 'patients' database.
"""
from pg import DB
import datetime

db = DB(dbname = "patient_db_test")
print(datetime.date.today())
#db.query("DROP TABLE patients;")
print(db.query('''create table patients(
	PHN CHAR(10) PRIMARY KEY,
	first_name text not null,
	last_name text not null,
	DOB DATE not null CHECK (DOB<current_date)
	)'''.format(datetime.date.today()))
	)
	
print(db.query("SELECT * from patients;"))
