import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation

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
    