#!/usr/bin/python3
"""Module for FileStorage class."""
import datetime
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """File to store retrieving data set."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary __objects.

        Returns:
            dict: Dictionary of objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id.

        Args:
            obj: Object to be added to __objects.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (__file_path).
    
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized_objects, file)

        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as File:
            serialized_objects = {key: v.to_dict() for key, v in FileStorage.__objects.items()}
            json.dump(serialized_objects, File)
    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }
        return classes

    def reload(self):
        """Reloads the stored objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as File:
            data = json.load(File)
            data = {key: self.classes()[value["__class__"]](**value)
                        for key, value in data.items()}
            FileStorage.__objects = data

    def attributes(self):
        """Returns the valid attributes and their types for each class."""
        attributes = {
            "BaseModel": {"id": str,
                          "created_at": datetime.datetime,
                          "updated_at": datetime.datetime},
            "User": {"email": str,
                     "password": str,
                     "first_name": str,
                     "last_name": str},
            "State": {"name": str},
            "City": {"state_id": str,
                     "name": str},
            "Amenity": {"name": str},
            "Place": {"city_id": str,
                      "user_id": str,
                      "name": str,
                      "description": str,
                      "number_rooms": int,
                      "number_bathrooms": int,
                      "max_guest": int,
                      "price_by_night": int,
                      "latitude": float,
                      "longitude": float,
                      "amenity_ids": list},
            "Review": {"place_id": str,
                       "user_id": str,
                       "text": str}
        }
        return attributes
