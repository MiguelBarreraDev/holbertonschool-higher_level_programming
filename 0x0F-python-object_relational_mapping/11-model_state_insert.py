#!/usr/bin/python3
"""
Script: Adds the State object “Louisiana” to the database hbtn_0e_6_usa
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
    try:
        new_row = State("Louisiana")
        session.add(new_row)
        session.commit()
    finally:
        session.close()

    rows = session.query(State).filter(State.name == "Louisiana")

    # Show response
    print(rows[0].id)

    # End session
    session.close()
