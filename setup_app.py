#!/bin/env python
# coding: utf-8

import socket
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

imageserver1 = model.ConfigImageServer()
imageserver1.url = 'http://127.0.0.1/iipsrv'
imageserver2 = model.ConfigImageServer()
imageserver2.url = 'http://%s/iipsrv' % socket.gethostbyname(socket.gethostname())


db.session.add_all([root, twitter, imageserver1, imageserver2])
db.session.commit()
