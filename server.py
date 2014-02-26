# coding: utf-8

import os, ConfigParser, hashlib
from flask import Flask, g, redirect, url_for, flash, request, render_template
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from flask.ext.sqlalchemy import SQLAlchemy
import model

config = ConfigParser.ConfigParser()
config.readfp(open('server.ini'))

app = Flask(__name__)
app.debug = config.getboolean("GLOBAL", "debug")
app.config['SECRET_KEY'] = config.get("GLOBAL", "secret")
app.config['SQLALCHEMY_DATABASE_URI'] = config.get("DATABASE", "sqlalchemy.url")
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
with app.app_context():
    g.db = db


@app.route('/')
def index():
    return render_template('index.htm')

@app.route('/login')
def login():
    return render_template('login.htm')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('logout successful!', 'success')
    return redirect('/')
    

@login_manager.user_loader
def load_user(userid):
    return db.session.query(model.User).filter(model.User.id == userid).first()

@app.route('/login_local', methods=['GET', 'POST'])
def login_local():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
    elif request.method == 'GET':
        username = request.args.get('username', '')
        password = request.args.get('password', '')
        
    user = db.session.query(model.User_local).filter(model.User_local.name == username).first()
    
    if not user:
        flash('login failed!', 'warning')
        return redirect('/login')
    if user.password == hashlib.sha512(password).hexdigest():
        flash('login successful!', 'success')
        login_user(user)
        return redirect('/')
    flash('login failed!', 'warning')
    return redirect('/login')


if __name__ == '__main__':
    app.run()

