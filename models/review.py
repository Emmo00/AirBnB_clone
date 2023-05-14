#!/usr/bin/python3
"""review module
Defines Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) == 0:
            self.place_id = ""
            self.user_id = ""
            self.text = ""
