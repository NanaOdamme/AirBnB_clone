#!/usr/bin/python3
"""this module creates a city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class inherits from BaseModel.
    """
    state_id = ""
    name = ""
