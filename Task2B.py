from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #prints the name of each station at which the current relative level is over 0.8, with the relative level alongside the name
    over_threshold = stations_level_over_threshold(stations,0.8)
    for station in over_threshold:
        print('{}, {}'.format(station[0], station[1]))
    

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()