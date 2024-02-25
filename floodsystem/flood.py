"""This module provides functions for analysis of the flood risk at weather stations

"""

from .utils import sorted_by_key
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol): #returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station
    stations_over = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == True:
    #        if MonitoringStation.relative_water_level(station) > tol:
                stations_over.append((station.name, MonitoringStation.relative_water_level(station)))
    sorted_by_key(stations_over,1)
    return stations_over