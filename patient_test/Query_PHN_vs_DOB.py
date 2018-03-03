import random
import names
import datetime
from pg import DB

"""
test_query.py
Input:
-A list of found potential PHNs
-A list of found potential DOB's

Output:
-A list of PHN -> DOB matches, and the full names of each match

IDEA:

Patient database structure:
(phn:"text" PRIMARY KEY, first_name:"text",last_name:"text",dob:"datetime.date type")

create 2 temp tables:
1) representing the found PHN nums
2) representing the found DOBs

Select first_name, last_name from (Select * from patients inner join found_phns on patients.phn=found_phns.phn as PHN_matches) 
										inner join Found_DOB on PHN_matches.DOB = Found_DOB.DOB


"""

#dummy example where we are trying to find the name Melvin Sanders, who corresponds to DOB=1918-9-17 and PHN=3751129774 
found_DOB = ["1918-9-17", "1975-6-2", "1986-8-7"]
found_PHN = ["3751129774","8374816353","1234567891"]

db = DB("patient_db_test")
print(db.query("SELECT * from patients"))


db.query("CREATE TABLE found_phns(phn text PRIMARY KEY);")
db.query("CREATE  TABLE found_dobs(dob date PRIMARY KEY);")
print(db.get_tables())
#each row must be in form of a tuple, even though it may only be 1 element per tuple
found_DOB_table = [tuple([x]) for x in found_DOB]
found_PHN_table = [tuple([x]) for x in found_PHN]
#print(found_PHN_table)
db.inserttable("public.found_phns", found_PHN_table)
db.inserttable("public.found_dobs", found_DOB_table)
print(db.query("select * from patients, found_phns, found_dobs where patients.phn=found_phns.phn and found_dobs.dob = patients.dob;"))


db.query("DROP TABLE found_phns")
db.query("DROP TABLE found_dobs")

