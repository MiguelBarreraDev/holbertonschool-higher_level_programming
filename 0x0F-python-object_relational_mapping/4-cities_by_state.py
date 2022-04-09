#!/usr/bin/python3
"""
Script: Lists all cities from the database hbtn_0e_4_usa
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
        """
        SELECT cities.id, cities.name, states.name FROM cities
        LEFT JOIN states ON cities.state_id = states.id;
        """
    )

    # Show
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
