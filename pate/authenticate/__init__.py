# coding: utf-8

from flask import Blueprint, render_template, flash, redirect
from flask.ext.login import login_user, logout_user, current_user, login_required

from local import login_local
from twitter import login_twitter, oauthorized_twitter

bp = Blueprint('authenticate', __name__)


@bp.route('/')
def index():
    return render_template('login.htm')
    

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash('logout successful!', 'success')
    return redirect('/')


bp.add_url_rule('/login_local', 'login_local', login_local, methods=['GET', 'POST'])

bp.add_url_rule('/login_twitter', 'login_twitter', login_twitter, methods=['GET', 'POST'])
bp.add_url_rule('/oauthorized_twitter', 'oauthorized_twitter', oauthorized_twitter, methods=['GET', 'POST'])