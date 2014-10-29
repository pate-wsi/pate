# coding: utf-8

from sqlalchemy import Column, Integer, Unicode, Boolean, DateTime
from pate.model import Base
import hashlib, datetime

class ConfigOAuthProvider(Base):
    __tablename__ = 'config_oauth'

    name = Column(Unicode(4), primary_key=True)
    active = Column(Boolean(), nullable=False, default=True)
    consumer_key = Column(Unicode(64))
    consumer_secret = Column(Unicode(64))


class ConfigImageServer(Base):
    __tablename__ = 'config_imageserver'

    id = Column(Integer, primary_key=True)
    active = Column(Boolean(), nullable=False, default=True)
    url = Column(Unicode(64), nullable=False)
