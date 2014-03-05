# coding: utf-8

from pate import db, model

def getOAuthCfg(type):
    try:
        cfg = db.session.query(model.ConfigOAuthProvider).filter(model.ConfigOAuthProvider.name == type).first()
    except:
        cfg = False
    if cfg:
        return cfg
    else:
        cfg = model.ConfigOAuthProvider()
        cfg.name = type
        cfg.active = False
        cfg.consumer_key = ' '
        cfg.consumer_secret = ' '
        return cfg
