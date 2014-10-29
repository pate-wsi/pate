# coding: utf-8

import requests
from flask import Blueprint, current_app, render_template, flash, url_for, redirect, request, jsonify, Response
from flask.ext.login import current_user, login_required
from pate.model import Basket, Slide, ConfigImageServer
from pate import db

bp = Blueprint('slide', __name__)


def get_img_url(filename):
    for imageserver in db.session.query(ConfigImageServer).all():
        url = '%s/?FIF=%s' % (imageserver.url, filename)
        size = requests.get('%s&OBJ=Max-size' % url)
        if not size.status_code == 200:
            continue
        return url
    return False


@bp.route('/view/<int:slide_id>')
def view_slide(slide_id):
    slide = db.session.query(Slide).filter(Slide.id == slide_id).one()
    return render_template('slide/viewer.htm', slide=slide)


@bp.route('/info/<int:slide_id>')
def info(slide_id):
    slide = db.session.query(Slide).filter(Slide.id == slide_id).one()
    for imageserver in db.session.query(ConfigImageServer).all():
        url = get_img_url('%i%s' % (slide.id, slide.file_extension))
        size = requests.get('%s&OBJ=Max-size' % url)
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


@bp.route('/imgproxy/<int:slide_id>')
def img_proxy(slide_id):
    slide = db.session.query(Slide).filter(Slide.id == slide_id).one()
    c = dict()
    c['height'], c['width'] = 400, 400
    for var in ['height', 'width']:
        if var in request.args: c[var] = int(request.args[var])
        if c[var] > 400: c[var] = 400
    url = get_img_url('%i%s' % (slide.id, slide.file_extension))
    return Response(
        requests.get('%s&WID=%i&HEI=%i&CVT=jpeg' % (url, c['width'], c['height'])).content,
        mimetype='image/jpeg')
