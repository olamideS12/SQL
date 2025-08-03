import sqlite3

database = "database.sqlite"

conn = sqlite3.connect(database)

print ("database connected successfully")

import pandas as pd
tables = pd.read_sql(""" 
select * from sqlite_master WHERE type = 'table';
""", conn)
print(tables)

Match = pd.read_sql("""
select * from Match;
""", conn)

#print(Match)

Max_min_margin = pd.read_sql("""
select Max(Win_Margin),Min(Win_Margin)
from Match;
""", conn)
#print (Max_min_margin)                                                                   

Match_winner7 = pd.read_sql("""
select * from Match 
where Match_winner == 7;
""", conn)
#print(Match_winner7)

City = pd.read_sql("""
select * from City;
""", conn)
#print(City)

Season = pd.read_sql("""
select * from Season;
""", conn)
print(Season)

New_team = pd.read_sql(""" 
select * from Team
where Team_name like '%D%';
""", conn)
#print(New_team)

Venue = pd.read_sql(""" 
select * from Venue;
                    
""",conn)
#print(Venue)


Eden_gardens = pd.read_sql("""
select count (distinct(venue_id)) from match
where Season_Id =5;
""",conn)
print(Eden_gardens)

Result = pd.read_sql("""
Select max(Win_Margin),min(Win_Margin),AVG(Win_Margin)
From Match; 
""",conn)
print(Result)