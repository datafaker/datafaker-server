#!/usr/bin/env python3

import env

import os.path

from flask import Flask, request
from flask_jwt_extended import JWTManager
from werkzeug.exceptions import NotFound

from consts import Constants

def create_app(static_options=dict(), configator=None):
    app = Flask(__name__, **static_options)
    #
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)
    ##----------------------------------------------------------------------------------------------------
    #
    @app.errorhandler(NotFound)
    def handle_404(e):
        return flask_util.response_with(flask_util.SERVER_ERROR_404)
    #
    ##----------------------------------------------------------------------------------------------------
    #
    @app.teardown_request
    def app_teardown_request(exception):
        pass
    #
    #
    return app


def create_app_with_static_folder(configator=None):
    return create_app(configator=configator, static_options = dict(
        static_url_path="/files",
        static_folder=os.path.join(os.getcwd(), "static")
    ))


if __name__ == '__main__':
    app = create_app_with_static_folder()
    app.run(host='0.0.0.0', port=7079, use_reloader=False, debug=True)
