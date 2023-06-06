#!/usr/bin/env python3
"""Authentication module"""

from uuid import uuid4
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """returns a hashed equivalent of given password"""
    password_byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(password_byte, salt)
    return hashed_pwd


def _generate_uuid() -> str:
    """Returns a string representation of a new UUID"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """return a User object"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> User:
        """Returns a boolean"""
        try:
            user = self._db.find_user_by(email=email)
            encoded_pwd = password.encode("utf-8")
            checkpwd = bcrypt.checkpw(encoded_pwd, user.hashed_password)
            return checkpwd
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """returns the session ID as a string"""
        try:
            user = self._db.find_user_by(email=email)
            user.session_id = _generate_uuid()
        except NoResultFound:
            return None
        return user.session_id
