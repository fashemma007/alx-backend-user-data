#!/usr/bin/env python3
"""Session authentication class handler"""
from base64 import b64decode
import binascii
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Sessions auth handler class"""
