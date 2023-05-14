#!/usr/bin/python3
"""state module
Defines the State class
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) != 0:
            self.name = ""
