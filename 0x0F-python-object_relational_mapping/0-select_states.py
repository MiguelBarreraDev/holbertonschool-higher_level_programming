#!/usr/bin/python3
"""
Script: Lists all states from the database hbtn_0e_0_usa
"""
if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    # Config object
    config = {
        'host': 'localhost',
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3],
        'port': 3306
    }

    # Start connection
    db = MySQLdb.connect(**config)
    cur = db.cursor()

    # Query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)
