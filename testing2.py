
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


stations = build_station_list()
update_water_levels(stations)

station = stations[3]
dt = 2
dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
plot_water_level_with_fit(station, dates, levels, 4)