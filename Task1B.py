from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    # Put code here that demonstrates functionality
    stations = build_station_list()
    p = [52.2053, 0.1218]
    print(stations_by_distance(stations, p))

if __name__ == "__main__":
    run()