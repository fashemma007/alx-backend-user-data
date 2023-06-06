#!/usr/bin/env python3
"""module docs for app.py"""
from flask import Flask, Response, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
