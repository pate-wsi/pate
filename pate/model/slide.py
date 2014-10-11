# coding: utf-8

import datetime
from sqlalchemy import ForeignKey, Column, Integer, Unicode, Boolean, DateTime
from sqlalchemy.orm import relationship, backref
from pate.model import Base, User, Basket


class Slide(Base):
    __tablename__ = 'slides'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(64), nullable=False)
    description = Column(Unicode(2018))
    upload_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    creation_date = Column(DateTime)    # date of the actual creation of the hardware slide
    file_extension = Column(Unicode(8), nullable=False)

    _basket = Column('basket', Integer, ForeignKey(Basket.id), nullable=False)
    basket  = relationship(Basket, backref="slides")
