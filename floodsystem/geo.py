# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqag
import haversine #Used in calculating shortest distance between two coordinates

def stations_by_distance(stations, p): #Function for generating a list of tuples (Station name , distance to coordinate p)
    
    stations_by_distance = []
    for station in stations: #iterate through each station

        d = haversine.haversine(station.coord, p) #calculate shortest distance of station coord to p
        stations_by_distance.append((station.name, d)) #adds tuple to list

    return sorted_by_key(stations_by_distance, 1)
    