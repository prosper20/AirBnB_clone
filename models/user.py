#!/usr/bin/python3
"""
User creation class
"""
from models.base_model import BaseModel

"""Defines attributes for user creation"""
class User(BaseModel):
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
