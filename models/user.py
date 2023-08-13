#!/usr/bin/python3
"""The User Class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    A subclass of BaseModel class that represents a user.

    Attributes:
        email (str): User's email address.
        password (str): User's password.
        first_name (str): User's first name.
        last_name (str): User's last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
