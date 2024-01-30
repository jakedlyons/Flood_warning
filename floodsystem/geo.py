# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqag
import haversine #Used in calculating shortest distance between two coordinates

def stations_by_distance(stations, p):
    
    stations_by_distance = []
    for station in stations:

        d = haversine.haversine(station.coord, p)
        stations_by_distance.append((station.name, d))

    return stations_by_distance
    