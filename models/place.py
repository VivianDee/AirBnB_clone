#!/usr/bin/python3
"""The Place Class"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    A subclass of BaseModel Class that gives users a place

    Attributes:
        city_id: City.id
        user_id: User.id
        name (str): Name of the state.
        description: Description of the location/place
        number_rooms: Number of rooms at the location
        number_bathrooms: Number of bathrooms at the location
        max_guest: Maximum number of accommodatable guests
        price_by_night: Price of a room for 1 night
        latitude: Geographical location
        longitude: Geographical location
        amenity_ids: Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
