from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list



def run():
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()

    #print how many rivers have at least one monitoring station and prints the first 10 of these rivers in alphabetical order
    rivers_list = rivers_with_station(stations)
    print(len(rivers_list) , 'rivers.')
    print('First 10 - {}' .format(rivers_list[:9]))

    #print the names of the stations located on the following rivers in alphabetical order
    stations_by_river_list = stations_by_river(stations)
    print(stations_by_river_list['River Aire'])
    print(stations_by_river_list['River Cam'])
    print(stations_by_river_list['River Thames'])



if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()