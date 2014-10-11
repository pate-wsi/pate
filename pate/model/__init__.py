# coding: utf-8

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from user import User, User_local, User_twitter
from config import ConfigOAuthProvider
from basket import Basket
from slide import Slide