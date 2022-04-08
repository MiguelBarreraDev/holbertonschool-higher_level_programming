#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""
Module description
"""

Base = declarative_base()


class State(Base):
    """
    Class definition
    """
    __tablename__ = 'states'
    id = Column(
        Integer, nullable=False, autoincrement='ignore_fk', primary_key=True
    )
    name = Column(String(128), nullable=False)
