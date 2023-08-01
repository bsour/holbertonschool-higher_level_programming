#!/usr/bin/python3
"""
Defines the State class and creates an instance of declarative_base
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

#create an instance of declarative_base
Base = declarative_base()
#define the sate class
class State(Base):
    """State class to represent the states table in the database"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    #constructor
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "<State(name='%s')>" % self.name
