"""This module contains a collection of functions related to representing
the water station data in visual plots.
"""
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation


def plot_water_levels(station, dates, levels):
    
    # Plot the water level against time
    plt.plot(dates, levels)

    #Plot horizontal lines for the typical low & high levels
    y_values = [station.typical_range[0], station.typical_range[1]]
    plt.hlines(y_values, xmin = dates[0], xmax = dates[-1], colors='r', linestyles='dashed', label='Typical High/Low Water Level')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels
    plt.legend() #Adds the low/high label
    plt.show()