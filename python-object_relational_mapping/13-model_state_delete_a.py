#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    usr = sys.argv[1]
    passwrd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(usr, passwrd, db),
        pool_pre_ping=True,
        echo=False
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).\
        filter(State.name.like('%a%')).all()
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()
    else:
        print("Nothing to delete")

    session.close()
