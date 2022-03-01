from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

### CODE FOR MAKING LIST OF TOWNS WITHOUT THE NECESSARY DATA ###
stations = build_station_list()
update_water_levels(stations)

unknown_risk_towns_set = set()
for station in inconsistent_typical_range_stations(stations):
    unknown_risk_towns_set.add(station.town)
### END OF CODE FOR MAKING LIST OF TOWNS WITHOUT THE NECESSARY DATA ###


### CODE FOR MAKING LIST OF TOWNS WITH LOW RISK LEVEL ###
low_risk_towns_set = set()

for station in stations:
    if station.relative_water_level() is not None and station.town is not None:
            if station.relative_water_level() < 1.2:
                low_risk_towns_set.add(station.town)
### END OF CODE FOR MAKING LIST OF TOWNS WITH LOW RISK LEVEL ###


### CODE FOR ASSESSING TOWNS WITH STATIONS IN RANGE 1.2 + ###
moderate_risk_towns_set = set()
high_risk_towns_set = set()
severe_risk_towns_set = set()

for station in stations:
    if station.relative_water_level() is not None and station.town is not None:
            if 1.2 < station.relative_water_level() < 1.5:
                if 1.2 < mean_level(station, 3) < 1.5:
                    if 1.2 < mean_level(station, 7) < 1.5:
                        high_risk_towns_set.add(station.town)
                    else:
                        moderate_risk_towns_set.add(station.town)
                else:
                    moderate_risk_towns_set.add(station.town)

    if station.relative_water_level() is not None and station.town is not None:
            if 1.5 < station.relative_water_level() < 2:
                if 1.5 < mean_level(station, 3) < 2:
                    if 1.5 < mean_level(station, 7) < 2:
                        severe_risk_towns_set.add(station.town)
                    else:
                        high_risk_towns_set.add(station.town)
                else:
                    moderate_risk_towns_set.add(station.town)

    if station.relative_water_level() is not None and station.town is not None:
            if station.relative_water_level() > 2:
                if mean_level(station, 3) > 2:
                    if mean_level(station, 7) > 2:
                        severe_risk_towns_set.add(station.town)
                    else:
                        severe_risk_towns_set.add(station.town)
                else:
                    high_risk_towns_set.add(station.town)

### CODE TO REMOVE TOWNS THAT ARE IN MORE THAN ONE CATEGORY, BY HIGH SEVERITY DOMINATING ###
severe_risk_towns = list(severe_risk_towns_set)

high_risk_towns = list(high_risk_towns_set - severe_risk_towns_set)

moderate_risk_towns = list(moderate_risk_towns_set - high_risk_towns_set - severe_risk_towns_set)

low_risk_towns = list(low_risk_towns_set - moderate_risk_towns_set - high_risk_towns_set - severe_risk_towns_set)

unknown_risk_towns = list(unknown_risk_towns_set - low_risk_towns_set - moderate_risk_towns_set - high_risk_towns_set - severe_risk_towns_set)
### END OF CODE TO REMOVE TOWNS THAT ARE IN MORE THAN ONE CATEGORY, BY HIGH SEVERITY DOMINATING ###
