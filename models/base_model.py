#!/usr/bin/python3
"""This script contains the base model"""

import uuid
from datetime import datetime
"""from models import storage     -uncomment for task 5"""


class BaseModel:

    """the class from which all  classes will inherit"""

    def __init__(self, *args, **kwargs):
        """construct for BaseModel

        Args:
            - *args: variable list of arguments
            - **kwargs: artibutrary keyword arguments
            - dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #storage.new(self)  uncomment this to test task 5

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
       # storage.save()  uncomment this to test task 5

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = type(self).__name__
        instance_dict["created_at"] = instance_dict["created_at"].isoformat()
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        return instance_dict
