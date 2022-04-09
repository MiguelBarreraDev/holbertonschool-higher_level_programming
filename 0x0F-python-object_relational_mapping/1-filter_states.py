#!/usr/bin/python3
"""
Script: Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
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
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Show
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
