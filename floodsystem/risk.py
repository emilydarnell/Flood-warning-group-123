def mean_level(station, days):
    # given a particular station and a number of days, work out what the average relative level is over these days
    # the easiest way is probably to average the actual water level over the last 'x' days
    # then put it into the formula for relative water level which ill put below
    return ('whatever the mean value is' - station.typical_range[0])/(station.typical_range[1]-station.typical_range[0])
