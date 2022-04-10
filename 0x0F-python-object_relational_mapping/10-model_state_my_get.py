#!/usr/bin/python3
"""
Script: Prints the State object with the name passed as argument
from the database
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, desc
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    # Config engine
    config = [argv[1], argv[2], argv[3]]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(*config)
    )
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query
    rows = session.query(State).filter(State.name == argv[4])

    # Show response
    try:
        print(rows[0].id)
    except Exception:
        print("Not found")
