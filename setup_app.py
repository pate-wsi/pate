#!/bin/env python
# coding: utf-8

from pate import db as db
from pate import model as model


model.Base.metadata.create_all(db.engine)

# root user
root = model.User_local()
root.name = u'root'
root.password = u'helloworld'

# oauth settings for twitter
twitter = model.ConfigOAuthProvider()
twitter.name = 'twtr'
twitter.consumer_key = 'xBeXxg9lyElUgwZT6AZ0A'
twitter.consumer_secret = 'aawnSpNTOVuDCjx7HMh6uSXetjNN8zWLpZwCEU4LBrk'


db.session.add_all([root, twitter])
db.session.commit()
