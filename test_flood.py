"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level

#Create a test station
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = (10.0, 20.0)
river = "River X"
town = "My Town"
latest_level = 19
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)

def test_stations_level_over_threshold():
    stations = [s]
    assert len(stations_level_over_threshold(stations, 0.8)) == 1 #check it includes the only test station

def test_stations_highest_rel_level():
    stations = [s]
    assert len(stations_highest_rel_level(stations, 2)) == 1 #check it returns the only test station