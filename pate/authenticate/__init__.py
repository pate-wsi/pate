# coding: utf-8

from flask import Blueprint
from flask import redirect, request, flash, request, render_template
from flask.ext.login import login_user, logout_user, current_user, login_required
from pate import db as db
from pate import model as model

bp = Blueprint('authenticate', __name__)


@bp.route('/login')
def login():
    return render_template('login.htm')
    

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash('logout successful!', 'success')
    return redirect('/')
    
    
@bp.route('/login_local', methods=['GET', 'POST'])
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
        return redirect('/authenticate/login')
    if user.check_password(password):
        flash('login successful!', 'success')
        login_user(user)
        return redirect('/')
    flash('login failed!', 'warning')
    return redirect('/authenticate/login')
