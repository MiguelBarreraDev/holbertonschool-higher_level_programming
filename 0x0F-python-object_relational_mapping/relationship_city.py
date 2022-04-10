#!/usr/bin/python3
"""
Module that defines the model for a table

Classes
-------
    City
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from relationship_state import Base


class City(Base):
    """
    City table model in the database.
    Allows the creation and insertion of records
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
