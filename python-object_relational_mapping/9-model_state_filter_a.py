#!/usr/bin/env python3
"""Script that lists all State objects containing the letter 'a'

from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine connecting to MySQL database using arguments passed in
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    # Bind session factory to engine
    Session = sessionmaker(bind=engine)

    # Create session inside context manager to guarantee connection closing
    with Session() as session:
        states = (
            session.query(State)
            .filter(State.name.like("%a%"))
            .order_by(State.id)
            .all()
        )

        for state in states:
            print("{}: {}".format(state.id, state.name))
