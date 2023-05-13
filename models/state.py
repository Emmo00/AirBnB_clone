#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if len(kwargs) != 0:
            self.name = ""
