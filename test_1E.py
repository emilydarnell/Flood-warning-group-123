from py import test
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


#checking that the number of stations on each river is decreasing#
def test_rivers_by_station_number():
    stations = build_station_list()
    test = rivers_by_station_number(stations, 20)
    index_list = []
    for i in range(len(test)):
        index_list.append(test[i][1])
    for j in range(len(index_list)-1):
        assert int(index_list[j]) >= int(index_list[j+1])

test_rivers_by_station_number()


print(test_rivers_by_station_number())