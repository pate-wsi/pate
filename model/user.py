# coding: utf-8

from sqlalchemy import Column, Integer, Unicode, Boolean
from model import Base
import hashlib

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(64), nullable=False)
    _type = Column('type', Unicode(4), nullable=False)
    active = Column(Boolean(), nullable=False)
    
    __mapper_args__ = {'polymorphic_on': _type}

    def __init__(self, name = None, active = True):
        self.name = name
        self.active = active

    def is_active(self):
        return self.active

    def get_id(self):
        return self.id

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


class User_local(User):
    __mapper_args__ = {'polymorphic_identity': 'locl'}

    type = 'local'
    _password = Column('password', Unicode(128))

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = hashlib.sha512(password).hexdigest()

    password = property(get_password, set_password)

    def check_password(self, password):
        hashed_pw = hashlib.sha512(password).hexdigest()
        if hashed_pw == self.password:
            return True
        else:
            return False


class User_twitter(User):
    __mapper_args__ = {'polymorphic_identity': 'twtr'}

    type = 'twitter'
