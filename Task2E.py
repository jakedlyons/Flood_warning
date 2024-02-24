#Import the functions and modules applied in this exercise
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    #Use Cam to test function
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
    

    dt = 10 #Number of days from now to be plotted
    
    #Create two lists of times with corresponding water levels
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))

    plot_water_levels(station_cam, dates, levels)
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***\n")
    run()