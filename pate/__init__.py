# coding: utf-8

import os, ConfigParser
from flask import Flask, g, redirect, url_for, flash, request, render_template
from flask.ext.login import LoginManager, current_user
from flask.ext.sqlalchemy import SQLAlchemy

config = ConfigParser.ConfigParser()
config.readfp(open('server.ini'))

app = Flask(__name__)
app.debug = config.getboolean("GLOBAL", "debug")
app.config['SECRET_KEY'] = config.get("GLOBAL", "secret")
app.config['SQLALCHEMY_DATABASE_URI'] = config.get("DATABASE", "sqlalchemy.url")
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

import model, authenticate


app.register_blueprint(authenticate.bp, url_prefix='/authenticate')


@login_manager.user_loader
def load_user(userid):
    return db.session.query(model.User).filter(model.User.id == userid).first()


@app.route('/')
def index():
    return render_template('index.htm')


if __name__ == '__main__':
    app.run()

