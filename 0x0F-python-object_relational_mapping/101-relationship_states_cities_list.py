#!/usr/bin/python3
"""
Script: Prints all City objects from the database
"""
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State, Base
    from relationship_city import City
    from sys import argv

    # Config engine
    config = [argv[1], argv[2], argv[3]]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(*config)
    )
    Base.metadata.create_all(engine)

    # # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querys
    rows = session.query(State).join(City).filter(State.id == City.state_id).\
        order_by(State.id, City.id)

    # Show result
    for row in rows:
        print(row.id, row.name, sep=": ")
        for sub_row in row.cities:
            print("\t{}: {}".format(sub_row.id, sub_row.name))

    # End session
    session.close()
