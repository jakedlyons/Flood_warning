import floodsystem.geo


"""Unit tests for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
import math
import haversine

def test_stations_by_distance(): #Test for function for generating a list of tuples (Station name , distance to coordinate p)
    
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = [s]
    d_function = stations_by_distance(stations, p = [0., 0.]) #Find distance between our defined station and p through function
    d_direct = haversine.haversine((-2., 4.), (0., 0.)) #Directly find distance between the two coords
    
    assert round(d_function[0][1], 8) == round(d_direct, 8) 