# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
#sorted by key allows you to sort a list by a certain part of each tuple#
from haversine import haversine

#CODE FOR TASK 1B#

def stations_by_distance(stations, p):
    #Calculates the distance of a station from a coordinate, p#
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


#CODE FOR TASK 1D.1#

def rivers_with_station(stations):
    #Finds a list of rivers with at least one monitoring station#
    #create empty set#
    set_of_rivers = set()
    for station in stations:
        set_of_rivers.add(station.river)
    return set_of_rivers


#CODE FOR TASK 1D.2#

def stations_by_river(stations):
    #Creates a dictionary with the river as key, and the stations on it as entries#
    #create empty dictionary#
    river_station_dict = {}
    for river in rivers_with_station(stations):
        stations_on_river = []
        for station in stations:
            if river == station.river:
                stations_on_river.append(station.name)
        river_station_dict[river] = stations_on_river
    return river_station_dict