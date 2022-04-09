#!/usr/bin/python3
"""
Script: Prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
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
    first_obj = session.query(State).first()

    # Show response
    print(first_obj.id, first_obj.name, sep=": ")
