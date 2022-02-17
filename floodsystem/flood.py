from .station import MonitoringStation
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    #create new dictionary to store the tuples#
    over_threshold_dict = []

    #check each station one by one#
    for station in stations:
        #check that there is no inconsistent data#
        if station.relative_water_level() is not None:
            #if the relative level is greater than the chosen tolerance, then add it to the dictionary#
            if station.relative_water_level() > tol:
                station_tol_tuple = (station.name, MonitoringStation.relative_water_level(station))
                over_threshold_dict.append(station_tol_tuple)
    #sort the dictionary into order by magnitude of relative water level#
    sorted_over_threshold_dict = sorted_by_key(over_threshold_dict, 1, reverse=True)
    return sorted_over_threshold_dict