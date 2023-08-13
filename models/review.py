#!/usr/bin/python3
"""The Review Class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    A subclass of BaseModel Class that handles Reviews

    Attributes:
        place_id (str): Place.id
        user_id (str): User.id
        text (str): review text
    """

    place_id = ""
    user_id = ""
    text = ""
