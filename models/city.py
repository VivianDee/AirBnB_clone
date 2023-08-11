#!/usr/bin/python3
"""The City Class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    A subclass of BaseModel Class that gives users a city

    Attributes:
        state_id (str): Id of State class
        name (str): Name of city.
    """

    state_id = ""
    name = ""
