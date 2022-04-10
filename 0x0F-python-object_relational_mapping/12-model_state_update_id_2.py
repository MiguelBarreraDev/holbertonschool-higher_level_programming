#!/usr/bin/python3
"""
Script: Changes the name of a State object from the database
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
    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()

    # End session
    session.close()
