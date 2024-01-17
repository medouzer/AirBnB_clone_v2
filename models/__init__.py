#!/usr/bin/env python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv
from models.engine.db_storage import DBStorage


t_storage = getenv('HBNB_TYPE_STORAGE')

if t_storage == "db":
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
