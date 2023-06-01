#!/usr/bin/env python3
"""Session authentication class handler"""
from base64 import b64decode
import uuid
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """Sessions auth handler class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user_id:
            * Return None if user_id is None
            * Return None if user_id is not a string
            * Return the Session ID if all is well
        """
        if user_id is None or (not isinstance(user_id, str)):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
