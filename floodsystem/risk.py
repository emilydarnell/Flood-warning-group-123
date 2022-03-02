from floodsystem.datafetcher import fetch_measure_levels
import statistics
import datetime

def mean_level(station, days_back):
    # given a particular station and a number of days, work out what the average relative level is over these days
    # the easiest way is probably to average the actual water level over the last 'x' days
    # then put it into the formula for relative water level which ill put below
    dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days = days_back))
    if len(levels) != 0:
        mean = statistics.mean(levels)
        relative_mean_level = (mean - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])
        return relative_mean_level
