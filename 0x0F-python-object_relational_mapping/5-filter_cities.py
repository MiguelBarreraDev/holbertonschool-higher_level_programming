#!/usr/bin/python3
"""
Script: Takes in the name of a state as an argument and lists all
cities of that state
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
        SELECT C.name FROM cities C
        INNER JOIN states S
        ON C.state_id = S.id
        WHERE S.name = %(state_name)s
        """,
        {'state_name': argv[4]}
    )

    # Show
    rows = cur.fetchall()
    list_names = list(map(lambda e: e[0], rows))
    print(*list_names, sep=', ')

    # Clean up
    cur.close()
    db.close()
