# IMPORT NECESSARY FUNCTIONS #
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    # DEMONSTRATION PROGRAM FOR TASK 1B #

    stations = build_station_list()
    city_centre_coord = (52.2053, 0.1218)
    distance_from_cam = stations_by_distance(stations, city_centre_coord)
    print("The 10 closest stations to Cambridge are: ", distance_from_cam[:10])
    print("The 10 furthest stations from Cambridge are: ", distance_from_cam[-10:])

if __name__ == "__main__":
    run()