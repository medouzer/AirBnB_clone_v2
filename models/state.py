#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

t_storage = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if t_storage == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        @property
        def cities(self):
            """getter attribute"""
            my_cities = []
            list_of_cities = list(models.storage.all(City).values())
            for city in list_of_cities:
                if city.state_id == self.id:
                    my_cities.append(city)
            return my_cities
