# coding: utf-8

from sqlalchemy import ForeignKey, Column, Integer, Unicode, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from pate.model import Base, User
import hashlib, datetime

#association_table = Table('basketToColaborator', Base.metadata,
#    Column('basket_id', Integer, ForeignKey('baskets.id')),
#    Column('user_id', Integer, ForeignKey('users.id'))
#)

class Basket(Base):
    __tablename__ = 'baskets'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(128), nullable=False)
    _owner = Column('owner', Integer, ForeignKey('users.id'), nullable=False)
    description = Column(Unicode(2048))
    
    owner = relationship("User", backref="baskets")
#    colaborators = relationship("User",
#                    secondary=association_table,
#                    backref="basket_colab")
