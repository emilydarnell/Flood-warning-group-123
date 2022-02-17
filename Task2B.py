from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    print(stations_level_over_threshold(stations, 0.8))

if __name__ == "__main__":
    run()
