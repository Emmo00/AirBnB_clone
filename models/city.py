#!/usr/bin/python3
"""city module
Defines City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) != 0:
            self.state_id = ""
            self.name = ""
