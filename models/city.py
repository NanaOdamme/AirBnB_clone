#!/usr/bin/python3
"""this module creates a city class"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City class inherits from BaseModel.
    """
    def __init__(self, *args, **kwargs):
        """Constructor for City"""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
