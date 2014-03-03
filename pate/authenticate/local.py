# coding: utf-8

from flask import redirect, request, flash
from flask.ext.login import login_user
from pate import db, model

#@current_app.route("/login_local")
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
        return redirect('/authenticate')
    if user.check_password(password):
        flash('login successful!', 'success')
        login_user(user)
        return redirect('/')
    flash('login failed!', 'warning')
    return redirect('/authenticate')
