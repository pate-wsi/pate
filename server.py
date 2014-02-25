# coding: utf-8

import os, ConfigParser, hashlib
from flask import Flask, redirect, url_for, flash, request
from flask.ext.login import LoginManager, login_user, logout_user, current_user
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import model

config = ConfigParser.ConfigParser()
config.readfp(open('server.ini'))

app = Flask(__name__)
app.debug = config.getboolean("GLOBAL", "debug")
app.config['SECRET_KEY'] = config.get("GLOBAL", "secret")
login_manager = LoginManager()
login_manager.init_app(app)

engine = create_engine(config.get("DATABASE", "sqlalchemy.url"),
           echo=config.getboolean("DATABASE", "sqlalchemy.echo"))
db_session = scoped_session(sessionmaker(bind=engine))


@app.route('/')
def hello_world():
    return 'Hello World!'

@login_manager.user_loader
def load_user(userid):
    return db_session.query(model.User).filter(model.User.id == userid).first()

@app.route("/login_local")
def login_local():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
    elif request.method == 'GET':
        username = request.args.get('username', '')
        password = request.args.get('password', '')

    user = db_session.query(model.User_local).filter(model.User_local.name == username).first()

    if not user:
        flash('login failed!')
        return redirect('/')
    if user.password == hashlib.sha512(password).hexdigest():
        flash('login successful!')
        login_user(user)
        return redirect('/')
    flash('login failed!')
    return redirect('/')


if __name__ == '__main__':
    app.run()

