#!/usr/bin/python3
"""
Script: Prints all City objects from the database
"""
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import State, Base
    from sys import argv

    # Config engine
    config = [argv[1], argv[2], argv[3]]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(*config)
    )
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querys
    rows_C = session.query(City).all()

    # Show result
    for row in rows_C:
        rows_S = session.query(State).filter(State.id == row.state_id)
        print(rows_S[0].name, row.id, row.name)

    # End session
    session.close()
