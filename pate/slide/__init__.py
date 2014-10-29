# coding: utf-8

import requests
from flask import Blueprint, current_app, render_template, flash, url_for, redirect, request, jsonify
from flask.ext.login import current_user, login_required
from pate.model import Basket, Slide, ConfigImageServer
from pate import db

bp = Blueprint('slide', __name__)


@bp.route('/view/<int:slide_id>')
def view_slide(slide_id):
    slide = db.session.query(Slide).filter(Slide.id == slide_id).one()
    return render_template('slide/viewer.htm', slide=slide)


@bp.route('/info/<int:slide_id>')
def info(slide_id):
    slide = db.session.query(Slide).filter(Slide.id == slide_id).one()
    for imageserver in db.session.query(ConfigImageServer).all():
        img = '%s/?FIF=%i%s' % (imageserver.url, slide.id, slide.file_extension)
        size = requests.get('%s&OBJ=Max-size' % img)
        if not size.status_code == 200:
            continue
        size = size.text.strip()
        width, height = size.lstrip('Max-size:').split(' ')
        return jsonify(dict(
            width  = width,
            height = height,
            filename = '%i%s' % (slide.id, slide.file_extension),
            name = slide.name
            ))


@bp.route('/getimageservers')
def get_image_servers():
    image_servers = []
    for server in db.session.query(ConfigImageServer).all():
        image_servers.append(server.url)
    return jsonify(dict(
        servers = image_servers))