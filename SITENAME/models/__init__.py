# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base

from SITENAME.config import sqla_uri, sqla_params

Base = declarative_base()


# define classes here
class Sample(Base):
    __tablename__ = 'samples'

    id = Column(Integer, primary_key=True, autoincrement=True)

engine = create_engine(sqla_uri, **sqla_params)
metadata = Base.metadata
