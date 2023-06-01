#!/usr/bin/env python3
""" Module of Sessions views
"""
from os import getenv
from flask import jsonify
from api.v1.views import app_views
from flask import request
from models.user import User


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login() -> str:
    """Login handler"""
    email = request.form.get("email")
    password = request.form.get("password")
    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        user = User.search({"email": email})
    except Exception:
        user = []

    if len(user) > 0:
        valid_pass = user[0].is_valid_password(password)
        if not valid_pass:
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth  # to avoid circular imports

        session_id = auth.create_session(user[0].id)
        user_json = jsonify(user[0].to_json())
        _cookie = getenv("SESSION_NAME")
        user_json.set_cookie(_cookie, session_id)
        return user_json
    else:
        return jsonify({"error": "no user found for this email"}), 404
