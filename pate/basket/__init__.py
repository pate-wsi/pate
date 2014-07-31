# coding: utf-8

from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask.ext.login import current_user
from pate.model import Basket
from pate import db

bp = Blueprint('basket', __name__)


@bp.route('/')
def index():
    return redirect(url_for('.my_baskets'))


@bp.route('/my_baskets')
def my_baskets():
    mybaskets = db.session.query(Basket).filter(Basket.owner == current_user)
    return render_template('basket/mybaskets.htm', mybaskets=mybaskets)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    if not 'basketname' in request.form: return render_template('basket/create.htm')
    basket = Basket()
    basket.name = request.form['basketname']
    if not request.form['basketdescription'] == '':
        basket.description = request.form['basketdescription']
    basket.owner = current_user
    db.session.add(basket)
    db.session.commit()
    flash('Created Basket "%s"' % request.form['basketname'], 'success')
    return redirect('/basket')


@bp.route('/<int:basket_id>')
def view_basket(basket_id):
    basket = db.session.query(Basket).filter(Basket.id == basket_id).one()
    return render_template('basket/basket.htm', basket=basket)