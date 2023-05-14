#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city.
    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) != 0:
            self.state_id = ""
            self.name = ""
