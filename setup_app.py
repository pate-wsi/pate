# coding: utf-8

from pate import db as db
from pate import model as model


model.Base.metadata.create_all(db.engine)

root = model.User_local()
root.name = u'root'
root.password = u'helloworld'

db.session.add(root)
db.session.commit()
