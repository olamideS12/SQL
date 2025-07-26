import sqlite3

database = "database.sqlite"

conn = sqlite3.connect(database)

print ("database connected successfully")

import pandas as pd
tables = pd.read_sql(""" 
select * from sqlite_master WHERE type = 'table';
""", conn)
