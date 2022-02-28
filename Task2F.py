# Demonstration showing plot of the 5 stations with the highest relative water levels as well as their best fit polynomials

import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_level_with_fit, plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def run():

   
    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    # Build list of the 5 stations at highest relative levels
    high_rel_level_stations = stations_highest_rel_level(stations, 5)
    print(high_rel_level_stations)
# Find dates and levels for each of these stations then add them to the plot
    # Get the names of the 5 highest level stations
    names = []
    for i in high_rel_level_stations:
        names.append(i[0])
    print(names)
    # Find each station
    names_with_id = []
    for i in names:
        station_name = i
        station_specific = None
        for station in stations:
            if station.name == station_name:
                station_specific = station
                names_with_id.append(station_specific)
                break
        # Check that each station could be found. Return if not found.
        if not station_specific:
            print("Station {} could not be found".format(station_name))
            return
        
    for i in names_with_id:     
        # Fetch data over past 2 days
        dt = 2
        dates, levels = fetch_measure_levels(
            station_specific.measure_id, dt=datetime.timedelta(days=dt))
        # Put this data onto a graph
        plot_water_level_with_fit(i, dates, levels, 4)

if __name__ == "__main__":
    run()