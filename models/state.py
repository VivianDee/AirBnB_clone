#!/usr/bin/python3
"""The State Class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    A subclass of BaseModel Class that gives users a state

    Attributes:
        name (str): Name of the state.
    """

    name = ""
