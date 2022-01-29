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

#CODE FOR TASK 1C#

def stations_within_radius(stations, centre, r):
    #empty list of stations within the radius#
    within_r = []
 #find distance of eaach station from centre#
    for station in stations:
        distance = haversine(station.coord, centre)
        #add any stations within the specified radius to a list#
        if distance <= r :
            within_r.append(station.name)
#sort list into alphabetical order by station name#
    sorted_within_r = within_r.sort()

    return within_r
    

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


#CODE FOR TASK 1E#

def rivers_by_station_number(stations, N):
    #Creates a list of rivers sorted by the number of stations on them#

    station_number_list = []
    dictionary = stations_by_river(stations)
    for i in dictionary.keys():
        n = len(dictionary[i])
        station_number_tuple = (i, n)
        station_number_list.append(station_number_tuple)

    sorted_station_by_number = sorted_by_key(station_number_list, 1, reverse=True)

    if sorted_station_by_number[N-1][1] != sorted_station_by_number[N][1]:
        return sorted_station_by_number[:N]
        #need some sort of recursion in the next part#
    elif sorted_station_by_number[N-1][1] == sorted_station_by_number[N][1]:
        for i in range(N+1, len(sorted_station_by_number)):
            extra = i - N
            if sorted_station_by_number[i-1][1] != sorted_station_by_number[i][1]:
                break
        return sorted_station_by_number[: N+extra]


        
