#!/usr/bin/python3
"""This is a Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for managing amenity objects"""

    def __init__(self, name="", *args, **kwargs):
        """menthod to initialize"""
        super().__init__(*args, **kwargs)
        self.name = name
