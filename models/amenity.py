#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


t_storage = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    if t_storage == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary="place_amenity",
                                       viewonly=False)
    else:
        name = ""
