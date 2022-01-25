from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    # DEMONSTRATION PROGRAM FOR TASK 1D.1 #
    stations = build_station_list()
    result = sorted(list(rivers_with_station(stations)))
    print(len(result))
    print(result[:10])

if __name__ == "__main__":
    run()

def run1():
    # DEMONSTRATION PROGRAM FOR TASK 1D.2 #
    stations = build_station_list()
    result2 = stations_by_river(stations)
    print("The stations on the River Aire are: ", sorted(result2['River Aire']))
    print("The stations on the River Cam are: ", sorted(result2['River Cam']))
    print("The stations on the River Thames are: ", sorted(result2['River Thames']))
    

if __name__ == "__main__":
    run1()