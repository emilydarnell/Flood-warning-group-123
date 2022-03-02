from floodsystem.risk import mean_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
import datetime
import statistics
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()
update_water_levels(stations)
station = stations[2]
print(station)

dt = 2
dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

mean = statistics.mean(levels)
relative_mean_level = (mean - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])
print(relative_mean_level)

print(mean_level(station, 2))
