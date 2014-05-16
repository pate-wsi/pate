# coding: utf-8

from flask import Blueprint, render_template, flash, url_for, redirect, request

bp = Blueprint('basket', __name__)


@bp.route('/')
def index():
    return render_template('basket/mybasket.htm')

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if not 'basketname' in request.form: return render_template('basket/create.htm')
    basketname = request.form['basketname']
    flash('Created Basket "%s"' % basketname, 'success')
    return redirect('/basket')
