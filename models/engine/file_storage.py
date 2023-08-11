#!/usr/bin/python3
"""The FileStorage class"""

import os
import copy
from datetime import datetime
import json


class FileStorage:
    """Serializes & deserializes instances to or from a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets the obj and the key in __objects"""
        if obj:
            self.__objects[(
                obj.__class__.__name__ + "." + obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        copy = {}
        for key, val in self.__objects.items():
            my_dict = val.to_dict()
            copy[key] = dict(my_dict)
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(copy, f)
        

    def storage_import(self, result):
        """Imports the storge module"""
        from models import storage
        from models.base_model import BaseModel
        objects = {}
        for obj_id, obj_data in result.items():
            obj = BaseModel(**obj_data)
            objects[obj_id] = obj
        return objects

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                result = json.load(f)
            self.__objects = self.storage_import(result)
