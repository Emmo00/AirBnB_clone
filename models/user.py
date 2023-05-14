#!/usr/bin/python3
"""Defines the User class."""
from .base_model import BaseModel


class User(BaseModel):
    """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
