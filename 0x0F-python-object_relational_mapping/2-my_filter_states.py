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
    q = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id"\
        .format(argv[4])
    cur.execute(q)

    # Show
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
