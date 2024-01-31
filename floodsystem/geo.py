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
    
def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    sorted_by_key(rivers,0)
    rivers = list(rivers)
    return rivers

def stations_by_river(stations):
    by_river = {i:[] for i in rivers_with_station(stations)}
    for station in stations:
        by_river[station.river].append(station.name)
    return by_river

def rivers_by_station_number(stations, N):
    by_station_number = {i:0 for i in rivers_with_station(stations)}
    for station in stations:
        by_station_number[station.river] += 1
    num = by_station_number
    selected = dict()
    for river in by_station_number:
        if by_station_number[river] >= num:
            selected[river] = by_station_number[river]
    return selected
