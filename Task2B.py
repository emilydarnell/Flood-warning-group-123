from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
import floodsystem.station as fs




stations = build_station_list()
update_water_levels(stations)

print(stations_level_over_threshold(stations, 0.8))