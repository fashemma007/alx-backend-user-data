#!/usr/bin/env python3
"""
Route module for the API
"""
import os
from os import getenv
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
AUTH_TYPE = getenv("AUTH_TYPE")

if AUTH_TYPE == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif AUTH_TYPE == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif os.getenv("AUTH_TYPE") == 'session_exp_auth':
    from api.v1.auth.session_exp_auth import SessionExpAuth
    auth = SessionExpAuth()
elif os.getenv("AUTH_TYPE") == 'session_db_auth':
    from api.v1.auth.session_db_auth import SessionDBAuth
    auth = SessionDBAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()
# print(auth.__class__)


@app.before_request
def b4_request():
    """before request"""
    paths = [
        '/api/v1/status/', '/api/v1/unauthorized/',
        '/api/v1/forbidden/', '/api/v1/auth_session/login/'
    ]
    # print(request.path)
    if auth.require_auth(request.path, paths):
        if auth.authorization_header(request) is None\
                and auth.session_cookie(request) is None:
            abort(401)
        if auth.current_user(request) is None:
            abort(403)

    request.current_user = auth.current_user(request)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ unauthorized, no access granted
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """Access denied to authenticated user"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    debug = getenv("DEBUG") or False
    app.run(host=host, port=port, debug=debug)
