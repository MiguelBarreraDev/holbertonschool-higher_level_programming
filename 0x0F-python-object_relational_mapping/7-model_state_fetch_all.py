#!/usr/bin/python3
"""
Script: Lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker

    # Config engine
    config = [argv[1], argv[2], argv[3]]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(*config)
    )
    Base.metadata.create_all(engine)

    # Open session and linking with the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    rows = session.query(State).all()

    # Show response
    for row in rows:
        print(row.id, row.name, sep=": ")
