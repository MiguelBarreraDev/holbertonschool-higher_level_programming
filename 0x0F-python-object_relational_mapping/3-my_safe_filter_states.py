#!/usr/bin/python3
"""
Script: Write one script that is safe from MySQL injections!
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
    cur.execute(
        "SELECT * FROM states WHERE name=%(param)s ORDER BY id",
        {'param': argv[4]}
    )

    # Show
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
