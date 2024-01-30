# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.
"""

from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
    rivers = set()
    for station in stations:
        rivers.add(station.river)
    sorted_by_key(rivers,0)
    rivers = list(rivers)
    return rivers

def stations_by_river(stations):
    by_river = dict.fromkeys(rivers_with_station(stations),[])
    for station in stations:
        by_river[station.river].append(station.name)
    return by_river

def rivers_by_station_number(stations, N):
    by_station_number = dict.fromkeys(rivers_with_station(stations),0)
    for station in stations:
        by_station_number[station.river] += 1
    num = by_station_number
    selected = dict()
    for river in by_station_number:
        if by_station_number[river] >= num:
            selected[river] = by_station_number[river]
    return selected
