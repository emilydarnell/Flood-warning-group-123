from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

#checking that each river only appears once in the list#
def test_rivers_with_station():
    stations = build_station_list()
    test = list(rivers_with_station(stations))
    for i in test:
        assert test.count(i) == 1

test_rivers_with_station()

def test_call():
    x = stations_by_river

test_call()