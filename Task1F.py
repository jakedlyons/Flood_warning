from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    # Put code here that demonstrates functionality
    stations = build_station_list()
    print(sorted(inconsistent_typical_range_stations(stations))) # Print alphabetically sorted inconsistent list

if __name__ == "__main__":
    run()