#!/usr/bin/env python3
"""
Main file
"""

from auth import Auth

auth = Auth()

email = "fasogbaemma@cool.guy"
password = "f@sogb@emm@"
user = auth.register_user(email, password)
valid_user = auth.valid_login(email, password)
if valid_user:
    print(f"Logged in as {email}")
else:
    print("Incorrect credentials")
session_id = auth.create_session(user.email)
found_user = auth.get_user_from_session_id(session_id)
print(found_user.email)


password = "f@@emm@"

valid_user = auth.valid_login(email, password)
if valid_user:
    print(f"Logged in as {email}")
else:
    print("Incorrect credentials")
session_id = user.session_id
found_user = auth.get_user_from_session_id(session_id)
print(found_user.email)

session_id = 'wrongsessionid'
found_user = auth.get_user_from_session_id(session_id)
print(found_user.email)
