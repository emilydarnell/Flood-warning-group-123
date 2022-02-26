from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    print(stations_highest_rel_level(stations, 10))

if __name__ == "__main__":
    run()