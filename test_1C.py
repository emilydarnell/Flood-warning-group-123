# IMPORT NECESSARY FUNCTIONS #
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

#tests that stations are put into alphabetical order#
def test_stations_within_radius1():
    stations = build_station_list()
    city_centre_coord = (52.2053, 0.1218)
    test = stations_within_radius(stations, city_centre_coord, 3)

    assert test == ['Bin Brook', 'Cambridge Jesus Lock']

test_stations_within_radius1()
#tests that only distances below r are included#
def test_stations_within_radius2():
    stations = build_station_list()
    city_centre_coord = (52.2053, 0.1218)
    test = stations_within_radius(stations, city_centre_coord, 0)

    assert test == []

test_stations_within_radius2()