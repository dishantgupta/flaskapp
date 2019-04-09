from flask import current_app as app


def get(key):
    return app.config.get(key)


def getall():
    return app.config
