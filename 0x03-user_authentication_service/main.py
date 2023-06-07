#!/usr/bin/env python3
"""
Main file
"""

from auth import Auth
session_id = '8836deab-0121-4140-ac4e-7e7d8697d95e'
auth = Auth()

user = auth.get_user_from_session_id(session_id)
print(user.email)
print(auth.create_session("unknown@email.com"))
