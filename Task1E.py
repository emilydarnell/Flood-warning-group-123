from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


stations = build_station_list()

def run():
    result = rivers_by_station_number(stations, 17)

    print(result)
    print(len(result))
    
if __name__ == "__main__":
    run()
