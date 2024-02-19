#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base

classes = {'State': State, 'City': City,
               'User': User, 'Place': Place,
               'Review': Review, 'Amenity': Amenity}

class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage"""
        hbnb_user = getenv("HBNB_MYSQL_USER")
        hbnb_pwd = getenv("HBNB_MYSQL_PWD")
        hbnb_host = getenv("HBNB_MYSQL_HOST")
        hbnb_db = getenv("HBNB_MYSQL_DB")
        hbnb_env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(hbnb_user,
                                             hbnb_pwd,
                                             hbnb_host,
                                             hbnb_db),
            pool_pre_ping=True,
        )

        if hbnb_env == "test":
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """query on the current database session"""
        result = {}
        for clas in classes:
            if cls is None or cls is classes[clas] or cls is clas:
                objects = self.__session.query(classes[clas]).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    result[key] = obj
        return (result)
    
    def new(self, obj):
        """add the object to the current database session"""
        # if obj:
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)
        
    def reload(self):
        """reload data"""
        Base.metadata.create_all(self.__engine)
        session_to_scop = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_to_scop)
    
    def close(self):
        """close session"""
        self.__session.close()
