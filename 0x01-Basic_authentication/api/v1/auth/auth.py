"""authentication class handler"""
from typing import List, TypeVar
from flask import request


class Auth():
    """authentication class handler"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        The require_auth function is a decorator that checks if the user has
        authenticated with the server.
        :param self: Represent the instance of the class
        :param path: str: Specify the path of the file that is being accessed
        :param excluded_paths: List[str]: Pass in a list of paths that should
        not be checked for authentication
        :return: A boolean value
        """
        return False

    def authorization_header(self, request=None) -> str:
        """works with the header tag"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """return the current user"""
        return None
