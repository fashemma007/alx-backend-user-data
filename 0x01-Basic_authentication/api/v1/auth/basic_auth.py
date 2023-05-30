#!/usr/bin/env python3
"""Basic authentication class handler"""
from base64 import b64decode
import binascii
from typing import Tuple
from api.v1.auth.auth import Auth


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
