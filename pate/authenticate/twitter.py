# coding: utf-8

from flask import redirect, request, flash, url_for, session
from flask.ext.login import login_user
from pate import db, model, oauth


twitter = oauth.remote_app(
    'twitter',
    consumer_key='xBeXxg9lyElUgwZT6AZ0A',
    consumer_secret='aawnSpNTOVuDCjx7HMh6uSXetjNN8zWLpZwCEU4LBrk',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
)


def login_twitter():
    callback_url = url_for('.oauthorized_twitter', next=request.args.get('next'))
    return twitter.authorize(callback=callback_url or request.referrer or None)


@twitter.authorized_handler
def oauthorized_twitter(resp):
    print resp
    if resp is None:
        flash('login failed!', 'warning')
    else:
        uid = resp['user_id']
        alias = resp['screen_name']
        user = db.session.query(model.User_twitter).filter(model.User_twitter.name == uid).first()
        if not user:
            user = model.User_twitter()
            user.name = uid
            db.session.add(user)
            db.session.commit()
        if user.alias != alias:
            user.alias = alias
            db.session.commit()
        login_user(user)
    return redirect(url_for('index'))
