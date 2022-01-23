from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

#testing whether the distances are increasing in the rnage 20 to 40#
def test_stations_by_distance():
    stations = build_station_list()
    test = stations_by_distance(stations, (52.2053, 0.1218))
    for i in range(20, 40):
        assert test[i][2] >= test[i-1][2]

test_stations_by_distance()