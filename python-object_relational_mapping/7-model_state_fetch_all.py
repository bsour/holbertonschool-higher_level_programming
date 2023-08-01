#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py \
        <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get MySQL connection details from command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            mysql_username, mysql_password, database_name
        ),
        pool_pre_ping=True,
    )

    # Bind the engine to the Base
    Base.metadata.bind = engine

    # Create a sessionmaker to interact with the database
    DBSession = sessionmaker(bind=engine)

    # Create a session
    session = DBSession()

    # Query all State objects from the database and sort them by id
    states = session.query(State).order_by(State.id).all()

    # Print the State objects
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
