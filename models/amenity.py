#!/usr/bin/python3
"""The Amenity Class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    A subclass of BaseModel Class that gives users an Amenity

    Attributes:
        name (str): The Amenity.
    """

    name = ""
