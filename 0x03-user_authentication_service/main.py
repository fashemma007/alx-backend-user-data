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
    print(f"Logged in as {email}\n")
else:
    print("Incorrect credentials\n")
session_id = auth.create_session(user.email)
found_user = auth.get_user_from_session_id(session_id)


print(f"Session id for {user.email}", user.session_id)

print(f"Destroying session of user {user.email}")
auth.destroy_session(user.id)

print("", user.session_id)
