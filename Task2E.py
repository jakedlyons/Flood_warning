#Import the functions and modules applied in this exercise
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #Make list of the 5 stations with the highest relative level
    highest_stations = stations_highest_rel_level(stations, 5)
    
    dt = 10 #Number of days from now to be plotted
    for station in highest_stations:
        #Create two lists of times with corresponding water levels
        dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))

        plot_water_levels(station, dates, levels)
    
if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***\n")
    run()