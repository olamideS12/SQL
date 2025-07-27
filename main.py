import sqlite3

database = "database.sqlite"

conn = sqlite3.connect(database)

print ("database connected successfully")

import pandas as pd
tables = pd.read_sql(""" 
select * from sqlite_master WHERE type = 'table';
""", conn)
#print(tables)

Match = pd.read_sql("""
select * from Match;
""", conn)

print(Match)

Max_min_margin = pd.read_sql("""
select Max(Win_Margin),Min(Win_Margin)
from Match;
""", conn)
print (Max_min_margin)

Match_winner7 = pd.read_sql("""
select * from Match 
where Match_winner == 7;
""", conn)
#print(Match_winner7)

City = pd.read_sql("""
select * from City;
""", conn)
#print(City)

Team = pd.read_sql("""
select * from Team;
""", conn)
#print(Team)

New_team = pd.read_sql(""" 
select * from Team
where Team_name like '%D%';
""", conn)
#print(New_team)