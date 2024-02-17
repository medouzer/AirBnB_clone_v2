#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage

t_storage = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all,delete", backref="state")
    if t_storage != "db":
        @property
        def cities(self):
            """getter attribute"""
            cities_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
