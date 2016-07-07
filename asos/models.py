from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings

DeclarativeBase = declarative_base()

def db_connect():
    """ performs db connect using db settings from settings.py.
        Returns sqlalchemy engine instance
        """
    # print ('db_cnnect\n\n')
    return create_engine(URL(**settings.DATABASE))

def create_jackets_table(engine):
    # print('create_jackets_table\n\n\n')
    DeclarativeBase.metadata.create_all(engine)

class Jackets(DeclarativeBase):
    """ Sqlalchemy Jackets model """
    __tablename__ = "jackets"

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    price_orig = Column('price_orig', String, nullable=True)
    price_cur = Column('price_cur', String)
    image_url_small = Column('image_url_small', String)
    image_url_large = Column('image_url_large', String)
