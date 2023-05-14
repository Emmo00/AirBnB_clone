#!/usr/bin/python3
"""user module
Defines the User class
"""
from .base_model import BaseModel


class User(BaseModel):
    """User class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
