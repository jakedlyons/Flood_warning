from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():

    stations = build_station_list() #Build station list
    p = [52.2053, 0.1218] #Define coordinate to find distance between itself and each station

    ordered_stations = stations_by_distance(stations, p)
    print('\nThe closest 10 stations to city centre are :\n', ordered_stations[0:10])
    print('\nThe furthest 10 stations to city centre are :\n', ordered_stations[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()