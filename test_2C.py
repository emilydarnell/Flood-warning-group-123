from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
#checks that there are the correct number of outputs, and that thay have been sorted into decreasing order#
def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    test = stations_highest_rel_level(stations, 100)
    for i in range(len(test)-1):
        assert len(test) == 100 and test[i][1] >= test[i+1][1]

test_stations_highest_rel_level()