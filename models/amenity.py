#!/usr/bin/python3
"""amenity module
Defines amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) != 0:
            self.name = ""
