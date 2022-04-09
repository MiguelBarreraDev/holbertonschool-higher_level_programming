#!/usr/bin/python3
"""
Module that defines the model for a table

Classes
-------
    State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State table model in the database.
    Allows the creation and insertion of records
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
