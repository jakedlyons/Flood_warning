from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    # Put code here that demonstrates functionality
    stations = build_station_list()
    p = [52.2053, 0.1218]
    ordered_stations = stations_by_distance(stations, p)
    print('The closest 10 stations to city centre are :', ordered_stations[0:10])
    print('The furthest 10 stations to city centre are :', ordered_stations[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()