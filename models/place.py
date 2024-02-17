#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import models

t_storage = getenv("HBNB_TYPE_STORAGE")

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))

class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    amenity_ids = []

    if t_storage != "db":
        @property
        def amenities(self):
            """
            get the list of Amenities linked to place
            """
            her_amenities = []
            all_aminities = list(models.storage.all(Amenity).values())
            for amenity in all_aminities:
                if amenity.id in self.amenity_ids:
                    her_amenities.append(amenity)
            return her_amenities

        @amenities.setter
        def amenities(self, value):
            """set amenities that handles append method for adding
            an Amenity.id to the attribute amenity_ids
            """
            if isinstance(value, "Amenity"):
                self.amenity_ids.append(value.id)
