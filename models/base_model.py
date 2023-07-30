#!/usr/bin/python3
""" The BaseModel """
import models
from uuid import uuid4
from datetime import datetime
from sqlalchemy import String, Column, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
""" calls the declarative_base function to create the base class for
the SQLAlchemy models.

so that SQLAlchemy handles the underlying database interactions. """


class BaseModel():
    """ BaseModel class that other models inherit from.

    all common attributes/methods for other classes """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """ constructor of a BaseModel """
        if kwargs:
            for key, value in kwargs.items():
                if not key == '__class__':
                    setattr(self, key, value)
        if id not in kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def __str__(self):
        """ Returning the instance in user friendly way
        print: [<class name>] (<self.id>) <self.__dict__> """

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())

    def __repr__(self):
        """ Returning the '__str__' result as a standard python expression """
        return self.__str__()
    
    def save(self):
        """ Saving to the file """
        self.created_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        dict_copy = dict(self.__dict__)
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy.pop('_sa_instance_state', None)
        return dict_copy
    
    def delete(self):
        models.storage.delete(self)
