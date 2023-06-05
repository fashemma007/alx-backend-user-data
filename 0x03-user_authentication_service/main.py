#!/usr/bin/env python3
"""
Main file
"""
from user import User

print(User.__tablename__)
users = (User.__dict__)


for column in User.__table__.columns:
    
    print("{}: {}".format(column, column.type))
