#!/usr/bin/python3
"""__init__ module"""
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
