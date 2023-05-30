#!/usr/bin/env python3
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

    def test_require_auth_true_1(self):
        """Test test_require_auth"""
        new_instance = Auth()
        self.assertEqual(new_instance.require_auth(
            "/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]), True)

    def test_require_auth_true_2(self):
        """Test test_require_auth empt list"""
        new_instance = Auth()
        self.assertEqual(new_instance.require_auth(
            "/api/v1/status/", []), True)

    def test_require_auth_missing_backslash(self):
        """Test test_require_auth"""
        new_instance = Auth()
        excld = ["/api/v1/status/", "/api/v1/users/"]
        self.assertEqual(new_instance.require_auth(
            "/api/v1/status", excld), False)
        self.assertEqual(new_instance.require_auth(
            "/api/v1/users", excld), False)

    def test_require_auth_true(self):
        """Test test_require_auth true"""
        new_instance = Auth()
        self.assertEqual(new_instance.require_auth(
            "/api/v1/forbidden/", ["/api/v1/status/"]), True)

    def test_authorization_header_none(self):
        """Test authorization_header"""
        new_instance = Auth()
        self.assertEqual(new_instance.authorization_header(), None)

    def test_current_user_none(self):
        """Test current_user"""
        new_instance = Auth()
        self.assertEqual(new_instance.current_user(), None)
