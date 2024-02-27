"""Unit tests for the analysis module"""

from floodsystem.analysis import polyfit
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def test_polyfit():

    #Get sample data
    # Build list of stations
    stations = build_station_list()

    # Station name to find
    station_name = "Cam"

    # Find station
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    # Check that station could be found. Return if not found.
    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return

    # Fetch data over past 2 days
    dt = 2
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    
    assert type(polyfit(dates, levels, 3)) == tuple #Test output of polyfit is a tuple
