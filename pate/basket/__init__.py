# coding: utf-8

from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask.ext.login import current_user
from pate.model import Basket
from pate import db

bp = Blueprint('basket', __name__)


@bp.route('/')
def index():
    return render_template('basket/mybasket.htm')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if not 'basketname' in request.form: return render_template('basket/create.htm')
    basket = Basket()
    basket.name = request.form['basketname']
    basket.owner = current_user
    db.session.add(basket)
    db.session.commit()
    flash('Created Basket "%s"' % request.form['basketname'], 'success')
    return redirect('/basket')
