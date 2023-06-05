"""Test Users"""
import unittest
from user import User


class TestClassInit(unittest.TestCase):
    """Users model"""
    users = (User.__dict__)

    def test_tablename(self):
        '''testers'''
        self.assertEqual("users", self.users["__tablename__"])
