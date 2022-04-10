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
        "mysql+mysqldb://{}:{}@localhost/{}".format(*config)
    )
    Base.metadata.create_all(engine)

    # # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querys
    new_state = State(name="California")
    session.add(new_state)
    session.commit()

    new_city = City(name="San Francisco", state_id=new_state.id)
    session.add(new_city)
    session.commit()

    rows_C = session.query(City).all()

    # End session
    session.close()
