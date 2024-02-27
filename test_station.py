# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation

#Create a test station
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (10.0, 20.0)
river = "River X"
town = "My Town"
latest_level = 15
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

def test_create_monitoring_station():

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

from floodsystem.station import inconsistent_typical_range_stations

def test_inconsistent_typical_range_stations() :

    stations = [s]

    assert len(inconsistent_typical_range_stations(stations)) == 0 #Check function outputs a list of length one as station is inconsistent

def test_relative_water_level():
    stations = s
    assert MonitoringStation.relative_water_level(stations) == 0.5 #Check realtive water level calculation