# IMPORT NECESSARY FUNCTIONS #
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

#tests that only distances above r are included#
def test_stations_within_radius():
    stations = build_station_list()
    city_centre_coord = (52.2053, 0.1218)
    test = stations_within_radius(stations, city_centre_coord, 0)

    assert test == []

test_stations_within_radius()