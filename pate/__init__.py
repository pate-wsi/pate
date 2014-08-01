# coding: utf-8

import os, ConfigParser
from flask import Flask, g, redirect, url_for, flash, request, render_template
from flask.ext.login import LoginManager, current_user
from flask.ext.sqlalchemy import SQLAlchemy
from flask_oauthlib.client import OAuth
from flask.ext.babel import Babel

config = ConfigParser.ConfigParser()
config.readfp(open('server.ini'))

app = Flask(__name__)
app.debug = config.getboolean("GLOBAL", "debug")
app.config['SECRET_KEY'] = config.get("GLOBAL", "secret")
app.config['SQLALCHEMY_DATABASE_URI'] = config.get("DATABASE", "sqlalchemy.url")
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
oauth = OAuth(app)
babel = Babel(app)


import model, authenticate, user, basket


app.register_blueprint(authenticate.bp, url_prefix='/authenticate')
app.register_blueprint(user.bp, url_prefix='/user')
app.register_blueprint(basket.bp, url_prefix='/basket')


@login_manager.user_loader
def load_user(userid):
    return db.session.query(model.User).filter(model.User.id == userid).first()


@app.route('/')
def index():
    return render_template('index.htm')


@app.template_filter('xprint')
def xprint(pobject):
    if pobject: return pobject
    return ''


if __name__ == '__main__':
    app.run()

