#!/usr/bin/python3
"""This is a Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    def __init__(self, name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
