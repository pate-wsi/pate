# coding: utf-8

from flask import redirect, request, flash, url_for
from flask.ext.login import login_user
from pate import db, model


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
        return redirect(url_for('authenticate.index'))
    if user.check_password(password):
        flash('login successful!', 'success')
        login_user(user)
        return redirect(url_for('index'))
    flash('login failed!', 'warning')
    return redirect(url_for('authenticate.index'))
