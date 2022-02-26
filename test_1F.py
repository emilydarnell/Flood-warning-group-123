from floodsystem.station import MonitoringStation

from floodsystem.stationdata import build_station_list

# tests that stations with no range data are called inconsistent #

def test_typical_range_consistent():

    test = MonitoringStation(None, None, None, None, None, None, None)
    stations = build_station_list()
    assert test.typical_range_consistent() == False

test_typical_range_consistent()