import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit

# CODE FOR TASK 2E #
# creating function that will plot water level against time#
def plot_water_levels(station, dates, levels):
    t = dates
    level = levels

# Plot
    plt.plot(t, level)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

# plot the typical high/low ranges on the same graph
    low_value = station.typical_range[0]
    high_value = station.typical_range[1]
    plt.axhline(low_value, 0, 1, color="red")
    plt.axhline(high_value, 0, 1, color = "red")
    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()

#CODE FOR 2F#

def plot_water_level_with_fit(station, dates, levels, p):
    t = dates
    level = levels

# Plot
    plt.plot(t, level)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

# plot the typical high/low ranges on the same graph
    low_value = station.typical_range[0]
    high_value = station.typical_range[1]
    plt.axhline(low_value, 0, 1, color="red")
    plt.axhline(high_value, 0, 1, color = "red")

 # add the polyfit to the graph #
    poly, shift = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    x_shifted = poly(x - shift)

    plt.plot(dates, x_shifted)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.show()