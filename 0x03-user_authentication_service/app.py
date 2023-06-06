#!/usr/bin/env python3
"""module docs for app.py"""
from flask import Flask, Response, abort, jsonify, request, make_response
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"], strict_slashes=False)
def welcome() -> Response:
    """root url"""
    message = {"message": "Bienvenue"}
    return jsonify(message), 200


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """register a new user"""
    credentials = request.form
    if 'email' not in credentials or\
            'password' not in credentials:
        return
    try:
        new_user = AUTH.register_user(credentials.get(
            'email'), credentials.get('password'))
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    # print(new_user.hashed_password)
    return jsonify({
        "email": f"{new_user.email}", "message": "user created"}), 200


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """login handler"""
    credentials = request.form
    if 'email' not in credentials or\
            'password' not in credentials:
        abort(401)
    email = credentials.get("email")
    password = credentials.get("password")
    valid = AUTH.valid_login(email, password)
    if valid:
        session_id = AUTH.create_session(email)
        response = make_response({"email": f"{email}", "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response, 200
    abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
