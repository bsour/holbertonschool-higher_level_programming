#!/usr/bin/python3
"""
Lists all State objects that contain t\
he letter 'a' from the database hbtn_0e_6_usa
Usage:
    ./9-model_state_filter_a.py \
<mysql_username> <mysql_password> <database_name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}',
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State objects that contain the letter 'a' in their names
    states_with_a = session.query(State)\
                           .filter(State.name.like('%a%'))\
                           .order_by(State.id).all()

    # Display the results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
