"""Unit test for the plot module"""

from floodsystem.station import MonitoringStation
import numpy as np
from floodsystem.plot import plot_water_levels


def test_plot_water_levels():
    #Create a test station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (1,5)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    x = np.linspace(0,10, 51) #Create a list from 0 - 10
    y = np.linspace(0,10, 51)

    plot_water_levels(s, x, y) #Test plot function has two horzionatal lines at y = 1 and y = 5 with a straight line of gradient 1

