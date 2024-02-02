from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    # Task 1C operation
    stations = build_station_list()
    centre = [52.2053, 0.1218]
    r = 10 #radius in kilometers, same as the output for distance from Haversine

    print(sorted(stations_within_radius(stations, centre, r)))

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***\n")
    run()