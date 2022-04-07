#!/usr/bin/python3
"""
Script: Filter states by user input
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

    # Query
    QUERY = "SELECT * FROM states WHERE name = '{}' ORDER BY id"\
        .format(argv[4])
    cur.execute(QUERY)

    # Show
    rows = cur.fetchall()
    for row in rows:
        print(row)
