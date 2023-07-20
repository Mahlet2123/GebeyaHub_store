#!/usr/bin/python3
"""__init__ module"""
from os import environ
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()
