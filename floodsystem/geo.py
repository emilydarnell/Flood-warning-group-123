# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
#sorted by key allows you to sort a list by a certain part of each tuple#
from haversine import haversine

def stations_by_distance(stations, p):

    #create empty list#
    station_distance_list = []
    
    #create tuples to add to the list#
    for station in stations:
        distance = haversine(station.coord, p)
        station_distance_tuple = (station.name, station.town, distance)
        station_distance_list.append(station_distance_tuple)

    #sort the list by the 2nd index in each tuple#
    sorted_station_by_distance = sorted_by_key(station_distance_list, 2, reverse=False)

    return sorted_station_by_distance