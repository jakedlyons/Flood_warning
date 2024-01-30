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
