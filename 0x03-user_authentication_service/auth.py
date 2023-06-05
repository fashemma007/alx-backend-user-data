#!/usr/bin/env python3
"""Authentication module"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """returns a hashed equivalent of given password"""
    password_byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password_byte, salt)
    return hashed_pwd
