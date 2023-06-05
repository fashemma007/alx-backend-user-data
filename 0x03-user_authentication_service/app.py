#!/usr/bin/env python3
"""module docs for app.py"""
from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=["GET"])
def welcome() -> dict:
    """root url"""
    message = {"message": "Bienvenue"}
    return jsonify(message), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
