# coding: utf-8

from flask import Blueprint, render_template, flash, redirect
from flask.ext.login import login_user, logout_user, current_user, login_required
from pate import db, model

bp = Blueprint('user', __name__)


@bp.route('/<int:uid>')
def profile(uid):
    user = db.session.query(model.User).filter(model.User.id == uid).first()
    return render_template('profile.htm', user=user)
