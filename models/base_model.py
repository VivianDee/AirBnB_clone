#!/usr/bin/python3
"""The BaseModel class"""


from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initializes the class with a unique id and time

        Args:
            id: Unique id of the class instance
            creted_at: The creation date and time
            updated_at: Time and date at which the class was updated

        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'created_at':
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == '__class__':
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the string representation of the class"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute: updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys and their values"""
        dic_rep = self.__dict__
        dic_rep["__class__"] = __class__.__name__
        for key, value in dic_rep.items():
            if key in ['updated_at', 'created_at']:
                dic_rep[key] = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dic_rep
