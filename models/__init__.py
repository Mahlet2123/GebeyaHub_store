#!/usr/bin/python3
from os import environ
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
