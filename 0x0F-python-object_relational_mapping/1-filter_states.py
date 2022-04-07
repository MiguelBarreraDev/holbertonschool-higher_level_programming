#!/usr/bin/python3
"""
Script:L ists all states with a name starting with N (upper N) 
from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

# Object config
config = {
    'host': 'localhost',
    'user': argv[1],
    'passwd': argv[2],
    'db': argv[3],
    'port': 3306
}

# Starting the connection
db = MySQLdb.connect(**config)
cur = db.cursor()

# Querys
cur.execute('SELECT * FROM states WHERE name LIKE "N%" ORDER BY id')

# Show
rows = cur.fetchall()
for row in rows:
    print(row)
