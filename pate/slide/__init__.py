# coding: utf-8

from flask import Blueprint, current_app, render_template, flash, url_for, redirect, request
from flask.ext.login import current_user, login_required
from pate.model import Basket, Slide
from pate import db

bp = Blueprint('slide', __name__)


@bp.route('/view/<int:slide_id>')
def view_slide(slide_id):
    slide = db.session.query(Slide).filter(Slide.id == slide_id).one()
    return render_template('slide/viewer.htm', slide=slide)
