#!/usr/bin/python3
"""The FileStorage class"""

import os
from datetime import datetime
import json


class FileStorage:
    """Serializes & deserializes instances to or from a JSON file"""

    __file_path = "file.json"
    __objects = {}
    __cls = ""

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets the obj and the key in __objects"""
        if obj:
            self.__cls = obj.__class__.__name__
            self.__objects[(
                obj.__class__.__name__ + "." + obj.id)] = obj.__dict__

    def save(self):
        """Serializes __objects to the JSON file"""
        copy = {outer_key: dict(
            inner_dict) for outer_key, inner_dict in self.__objects.items()}
        for value in copy.values():
            if 'updated_at' in value and type(value['updated_at']) != str:
                value['updated_at'] = value[
                    'updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
            value['__class__'] = self.__cls
            if 'created_at' in value and type(value['created_at']) != str:
                value['created_at'] = value[
                    'created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(copy, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                self.__objects = json.load(f)
        for key, value in self.__objects.items():
            value['updated_at'] = datetime.strptime(
                value['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            value['created_at'] = datetime.strptime(
                value['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            del (value['__class__'])
