# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqa
import haversine #Used in calculating shortest distance between two coordinates

def stations_by_distance(stations, p): #Function for generating a list of tuples (Station name , distance to coordinate p)
    
    stations_by_distance = []
    for station in stations: #iterate through each station

        d = haversine.haversine(station.coord, p) #calculate shortest distance of station coord to p
        stations_by_distance.append((station.name, d)) #adds tuple to list

    return sorted_by_key(stations_by_distance, 1)
    
def rivers_with_station(stations): #Task1D1 returns a container (list/tuple/set) with the names of the rivers with a monitoring station
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    sorted_by_key(rivers,0)
    rivers = list(rivers)
    return rivers

def stations_by_river(stations): #Task1D maps river names (the ‘key’) to a list of station objects on a given river
    by_river = {i:[] for i in rivers_with_station(stations)}
    for station in stations:
        by_river[station.river].append(station.name)
    return by_river

def rivers_by_station_number(stations, N):  #return a list of (river name, number of stations) tuples, sorted by the number of stations
    by_station_number = {i:0 for i in rivers_with_station(stations)}
    for station in stations:
        by_station_number[station.river] += 1
    river_list = list()
    for river in by_station_number.keys():
        river_list.append((river, by_station_number[river]))
    river_list.sort(key=lambda x:x[1], reverse=True)
    selected = river_list[0:N-1]
    extra_count = 0
    while river_list[N + extra_count][1] == river_list[N-1][0]:
        selected.append(river_list[N + extra_count])
    return selected
