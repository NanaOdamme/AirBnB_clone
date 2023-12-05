#!/usr/bin/python3
"""This module creates a User class that inherits from base model"""
from models.base_model import BaseModel


class User(BaseModel):
    """add user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
