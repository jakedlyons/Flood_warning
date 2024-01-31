from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list



def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # prints the list of (river, number stations) tuples when N = 9.
    print(rivers_by_station_number(stations,9))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()