"""This module contains a collection of functions related to representing
the water station data in visual plots.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime, timedelta
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit


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

def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    x_plot = np.linspace(x[0], x[-1], 100)
    
    plt.plot(dates, levels, color = 'red', label = 'Water Level') #Plot actual water level data
    plt.plot(x_plot, poly(x_plot - x[0]), color = 'blue', label = 'Polyfit Water Level')

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
    