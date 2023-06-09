#!/usr/bin/env python3
"""Session authentication class handler"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User
# from base64 import b64decode
# from typing import Tuple, TypeVar


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

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None or (not isinstance(session_id, str)):
            return None
        user_id = self.user_id_by_session_id.get(session_id)
        return user_id

    def current_user(self, request=None):
        """returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        current_user = User.get(user_id)
        return current_user

    def destroy_session(self, request=None):
        """
        destroy_session function
        """
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        if not self.user_id_for_session_id(session_id):
            return False

        del self.user_id_by_session_id[session_id]
        return True
