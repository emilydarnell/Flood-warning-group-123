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

    dt = 4
    # Find each station
    for i in names:
        for station in stations:
            if station.name == i:
                try:
                    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
                    plot_water_level_with_fit(station, dates, levels, 4)
                except:
                    ValueError
                    print('Invalid data for this station:{}'.format(i))
                    pass

if __name__ == "__main__":
    run()