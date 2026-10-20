#!/usr/bin/env python3
"""This script lists all states from the database hbtn_0e_0_usa
where name matches the argument provided by the user.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State table for the first state with the given name
    state = session.query(State).order_by(State.id.asc()).first()

    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()
