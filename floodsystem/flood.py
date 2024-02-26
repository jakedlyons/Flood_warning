"""This module provides functions for analysis of the flood risk at weather stations

"""

from .utils import sorted_by_key
from .station import MonitoringStation

def stations_level_over_threshold(stations, tol): #returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station
    stations_over = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == True:
            if MonitoringStation.relative_water_level(station) != None:
                if MonitoringStation.relative_water_level(station) > tol:
                    stations_over.append((station.name, MonitoringStation.relative_water_level(station)))
    stations_over = sorted_by_key(stations_over,1,True)
    return stations_over

def stations_highest_rel_level(stations, N): #returns a list of the N stations (objects) at which the water level, relative to the typical range, is highest
    stations_rel = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == True:
            if MonitoringStation.relative_water_level(station) != None:
                    stations_rel.append((station, MonitoringStation.relative_water_level(station)))
    stations_rel = sorted_by_key(stations_rel,1,True)
    if N < len(stations_rel):
        stations_highest = stations_rel[:N-1]
    else:
        stations_highest = stations_rel
    return stations_highest