from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
#checks that all data included is over the tolerance, and that thay have been sorted into decreasing order#
def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    test = stations_level_over_threshold(stations, 0.8)
    for i in range(len(test)-1):
        assert test[i][1] > 0.8 and test[i][1] >= test[i+1][1]

test_stations_level_over_threshold()