#!/usr/bin/python3
"""This module defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Class for serializing and deserializing objects to and from JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                obj_dict = json.load(file)
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name)(**value))
        except FileNotFoundError:
            pass

