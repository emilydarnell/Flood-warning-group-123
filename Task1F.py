from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():

# shows list of inconsistent data #
    stations = build_station_list()
    inconsistent = [i.name for i in inconsistent_typical_range_stations(stations)]
    print(sorted(inconsistent))

if __name__ == "__main__":

    run()
