#!/usr/bin/python3
# State class definition that inherits from Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()

# Define the State class
class State(Base):
    """State class to represent the states table in the database"""

    # Table name
    __tablename__ = 'states'

    # Columns
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Constructor
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<State(name='%s')>" % self.name
        
