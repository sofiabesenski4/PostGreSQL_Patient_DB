#insert_dummy_data.py
import random
import names
import datetime
from pg import DB
"""
Feb 27 2018
This script should be run to enter some patients into the table called 'patients' in the database called 'patient_db_test'


DATE formats:
YMD - year-month-day is the most desirable format, considered ISO 8601 standards
"""

def PHN_gen():
	return "{0:010d}".format(random.randint(0,10000000000))
def patient_data_row_gen():
	#in the form (phn:"text", first_name:"text",last_name:"text",dob:"datetime.date type")
	year_list = [x for x in range(1910,2019)]
	month_list = [x for x in range(1,13)]
	day_list = [x for x in range(1,31)]
	DOB = datetime.datetime(year = int(random.randrange(1910,2019)),month =int(random.randrange(1,13)), day =int(random.randrange(1,31))).date()
	return (PHN_gen(), names.get_first_name(), names.get_last_name(), str(DOB))

db = DB("patient_db_test")
table_name = db.get_tables()
print(table_name)
print(db.get_attnames(table_name[0]))

dummy_data = [ patient_data_row_gen() for x in range(10)]
print(dummy_data)

db.inserttable(table_name[0], dummy_data)
