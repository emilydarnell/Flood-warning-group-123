# IMPORT NECESSARY FUNCTIONS #
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    # DEMONSTRATION PROGRAM FOR TASK 1C #

    stations = build_station_list()
    city_centre_coord = (52.2053, 0.1218)
    within_r = stations_within_radius(stations, city_centre_coord, 10)
    print("The stations withing 10km of Cambridge are: ", within_r)

if __name__ == "__main__":
    run()