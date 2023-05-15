#!/usr/bin/python3
"""user module
Defines the User class
"""
from .base_model import BaseModel


class User(BaseModel):
    """User class.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
