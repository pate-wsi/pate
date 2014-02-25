# coding: utf-8

import os
import ConfigParser
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
import model

config = ConfigParser.ConfigParser()
config.readfp(open('server.ini'))

engine = create_engine(config.get("DATABASE", "sqlalchemy.url"),
           echo=config.getboolean("DATABASE", "sqlalchemy.echo"))
#metadata = MetaData()
#metadata.create_all(engine)
model.Base.metadata.create_all(engine) 
db_session = scoped_session(sessionmaker(bind=engine))

root = model.User_local()
root.name = 'root'
root.password = 'helloworld'

db_session.add(root)
db_session.commit()
