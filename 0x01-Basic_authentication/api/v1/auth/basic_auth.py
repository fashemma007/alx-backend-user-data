#!/usr/bin/env python3
"""Basic authentication class handler"""
from base64 import b64decode
import binascii
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """inherits from Auth"""

    def extract_base64_authorization_header(self, authorization_header: str)\
            -> str:
        '''returns the Base64 part of the Authorization header'''
        if authorization_header is None\
                or (not isinstance(authorization_header, str))\
                or (not authorization_header.startswith("Basic ")):
            return None
        else:
            return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64
        """
        if base64_authorization_header is None\
                or (not isinstance(base64_authorization_header, str)):
            return None
        try:
            result = b64decode(base64_authorization_header).decode('utf-8')
            return result
        except binascii.Error:
            return None
        except UnicodeDecodeError:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None\
                or (not isinstance(decoded_base64_authorization_header, str))\
                or (":" not in decoded_base64_authorization_header):
            return None, None
        username, passwrd = decoded_base64_authorization_header.split(":")
        return (username, passwrd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password"""
        users = User.search({'email': user_email})
        if user_email is None or user_pwd is None\
                or (not isinstance(user_email, str)) or users is None\
                or (not isinstance(user_pwd, str)):
            return None
        # users = []
        # [print(user.__dict__) for user in users]
        for user in users:
            if user.is_valid_password(user_pwd):
                return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the user from a request.
        """
        auth_header = self.authorization_header(request)
        b64_auth_token = self.extract_base64_authorization_header(auth_header)
        auth_token = self.decode_base64_authorization_header(b64_auth_token)
        email, password = self.extract_user_credentials(auth_token)
        return self.user_object_from_credentials(email, password)
