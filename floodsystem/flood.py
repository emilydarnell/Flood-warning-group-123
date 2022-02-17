from .station import MonitoringStation
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    
    over_threshold_dict = []
    for station in stations:
        if station.relative_water_level() is not None:
            if station.relative_water_level() > tol:
                station_tol_tuple = (station.name, MonitoringStation.relative_water_level(station))
                over_threshold_dict.append(station_tol_tuple)
    sorted_over_threshold_dict = sorted_by_key(over_threshold_dict, 1, reverse=True)
    return sorted_over_threshold_dict