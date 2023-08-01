#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from model_city import City

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

    cities = session.query(State, City).\
        filter(State.id == City.state_id).order_by(City.id).all()
    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
