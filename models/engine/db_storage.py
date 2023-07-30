#!/usr/bin/python3
""" the database storage engine """
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.user_profile import UserProfile
from models.category import Category
from models.product import Product
from models.product_image import ProductImage
from models.review import Review
from models.cart import Cart
from models.cart_item import CartItem
from models.order import Order
from models.order_item import OrderItem
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {
        'User': User,
        'Category': Category,
        'Product': Product,
        'Review': Review,
        'Cart': Cart,
        'CartItem': CartItem,
        'Order': Order,
        'OrderItem': OrderItem,
        'UserProfile': UserProfile,
        'ProductImage': ProductImage
        }

class DBStorage():
    """ The DBStorage class """
    __engine = None
    __seission = None

    """
    The Session in SQLAlchemy is an object that represents a transactional
    scope for interacting with the database.

    Sessions are used to query, add, update, and delete data from the
    database using Python objects (models) instead of raw SQL queries.

    The session acts as a temporary workspace for changes to the objects,
    and these changes are eventually flushed (written) to the database
    when the session is committed.
    """

    def __init__(self):
        """Instantiate a DBStorage object"""
        ONLINE_STORE_MYSQL_USER = getenv('ONLINE_STORE_MYSQL_USER')
        ONLINE_STORE_MYSQL_PWD = getenv('ONLINE_STORE_MYSQL_PWD')
        ONLINE_STORE_MYSQL_HOST = getenv('ONLINE_STORE_MYSQL_HOST')
        ONLINE_STORE_MYSQL_DB = getenv('ONLINE_STORE_MYSQL_DB')
        ONLINE_STORE_ENV = getenv('ONLINE_STORE_ENV')

        """ 
        The create_engine function is used to create a new SQLAlchemy 
        engine that connects to the database.

        The Engine in SQLAlchemy represents the interface to the database.
        used to establish a connection to the database and execute raw
        SQL statements.
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(ONLINE_STORE_MYSQL_USER,
                                             ONLINE_STORE_MYSQL_PWD,
                                             ONLINE_STORE_MYSQL_HOST,
                                             ONLINE_STORE_MYSQL_DB),
                                      pool_pre_ping=True)
        """
        pool_pre_ping=True, SQLAlchemy will perform a "ping" on the
        database connections in the connection pool before they are used.

        A "ping" is a lightweight test query that checks if the
        connection to the database is still alive and valid.
        """
        if ONLINE_STORE_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session (self.__session)
        all objects depending of the class name (argument cls)

        if cls=None, query all types of objects

        return a dictionary:
            key = <class-name>.<object-id>
            value = object
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key]=obj
        return (new_dict)

    def get(self, cls, id):
        """
        query on the current database session (self.__session)
        an object based on the class and its ID, or None
        """
        if cls and id and type(id) is str:
            if (type(cls) is not str):
                cls = cls.__name__
            return self.all().get(cls + '.' + id)
        return None

    def count (self, cls=None):
        """ Counting the number of objects in the database """
        if cls:
            if type(cls) is not str:
                cls = cls.__name__
            return len(self.all(cls))
        return len(self.all())

    def new(self, obj):
        """ Adds the given object (obj) to the current database session. """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes made in the current database session
        to the database.
        """
        self.__session.commit()

    def close(self):
        """
        Closing the session is crucial to release any database connections
        and resources acquired during the session's use.

        This helps to manage resources efficiently, especially in long-running
        applications where multiple sessions may be created and closed over time.
        """
        self.__session.close()

    def delete(self, obj=None):
        """
        Deletes the given object (obj) from the current database
        session if it is not None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        setting up the necessary tables in the database and
        creating a new session.

        The create_all method automatically generates the necessary SQL
        to create tables that correspond to the defined classes (models)
        """
        
        Base.metadata.create_all(self.__engine)
        """ This line creates all the tables defined in the Base """
        
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        """
        This line creates a sessionmaker object, which acts as a factory for
        creating new sessions. The sessionmaker is bound to the database engine 
        (self.__engine), which means it knows how to interact with the database.
        """
        
        Session = scoped_session(session_factory)
        """
        This line creates a scoped_session using the session_factory.

        The scoped_session is a thread-safe version of a session that can be used
        across multiple threads without causing issues. It provides a way to manage
        the database session's lifecycle in a multi-threaded environment.
        """
        self.__session = Session

    def user_by_email(self, email):
        """ A method to retrieve a user by email """
        user =  self.__session.query(User).filter(User.email == email).first()
        if user:
            return user
        return None


    def user_by_id(self, user_id):
        """ A method to retrieve a user by ID """
        user =  self.__session.query(User).filter(User.id == user_id).first()
        if user:
            return user
        return None

    def serve_user(self, user):
        default_cart = Cart()
        default_cart.user_id = user.id
        self.new(default_cart)
        self.save()
        return default_cart
