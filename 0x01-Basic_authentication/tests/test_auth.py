"""Test Auth class and methods"""
import unittest
from api.v1.auth.auth import Auth


class TestAuth(unittest.TestCase):
    """Test Auth class and methods"""

    def test_require_auth_false(self):
        """Test require"""
        new_instance = Auth()
        self.assertEqual(new_instance.require_auth(
            "/api/v1/status/", ["/api/v1/status/"]), False)

    def test_authorization_header_none(self):
        """Test authorization_header"""
        new_instance = Auth()
        self.assertEqual(new_instance.authorization_header(), None)

    def test_current_user_none(self):
        """Test current_user"""
        new_instance = Auth()
        self.assertEqual(new_instance.current_user(), None)
