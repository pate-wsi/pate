# coding: utf-8

from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask.ext.login import current_user
from flask.ext.babel import gettext
from pate.model import Basket
from pate import db

bp = Blueprint('basket', __name__)


@bp.route('/')
def index():
    return redirect(url_for('.my_baskets'))


@bp.route('/<int:basket_id>')
def view_basket(basket_id):
    basket = db.session.query(Basket).filter(Basket.id == basket_id).one()
    return render_template('basket/basket.htm', basket=basket)


@bp.route('/my_baskets')
def my_baskets():
    mybaskets = db.session.query(Basket).filter(Basket.owner == current_user)
    return render_template('basket/mybaskets.htm', mybaskets=mybaskets)


@bp.route('/create')
@bp.route('/change/<basketid>', methods=['GET', 'POST'])
def change(basketid=None):
    if basketid:
        basket = db.session.query(Basket).filter(Basket.id == basketid).one()
        msg = [ gettext(u'Basket information has been updated'), 'success' ]
    else:
        basket = Basket()
        db.session.add(basket)
        msg = [ gettext(u'Basket has been created'), 'success' ]
    if 'basketname' in request.form: basket.name = request.form['basketname']
    basket.owner = current_user
    if 'basketdescription' in request.form:
        if not request.form['basketdescription'] == '':
            basket.description = request.form['basketdescription']
    if basket.name and 'basketdescription' in request.form:
        db.session.commit()
        flash(msg[0], msg[1])
    return render_template('basket/change.htm', basket=basket)
