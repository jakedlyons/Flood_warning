import math
import haversine

"""Unit tests for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

#Create a test station
s_id = "test-s-id"
m_id = "test-m-id"
label = "some station"
coord = (-2.0, 4.0)
trange = None
river = "River X"
town = "My Town"
s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

def test_stations_by_distance(): #Test for function for generating a list of tuples (Station name , distance to coordinate p)

    stations = [s]
    d_function = stations_by_distance(stations, p = [0., 0.]) #Find distance between our defined station and p through function
    d_direct = haversine.haversine((-2., 4.), (0., 0.)) #Directly find distance between the two coords

    assert round(d_function[0][1], 8) == round(d_direct, 8)

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def test_stations_within_radius():

    stations = [s]
    assert len(stations_within_radius(stations, centre = (-2., 4.) , r = 0.01)) == 1 #Test output list has length one with centre equal to stations s coordinate.


