# demonstration of plotting water levels and typical high/low ranges #
# plotting water level over the past 10 days in the 5 stations with greatest relative water level #

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels

