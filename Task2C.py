from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #prints the names of the 10 stations at which the current relative level is highest, with the relative level beside each station name
    highest = stations_highest_rel_level(stations, 10)
    for station in highest:
        print('{}, {}'.format(station[0], station[1]))

if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()