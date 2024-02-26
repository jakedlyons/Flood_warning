from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    #build lists of stations of different level. 
    #Stations with relative water level over 1.0 is considered severe. 
    #Stations with relative water level between 0.8 and 1.0 is considered high. 
    #Stations with relative water level between 0.6 and 0.8 is considered moderate. 
    #Stations with relative water level under 0.6 is considered low.
    severe = [i[0] for i in stations_level_over_threshold(stations,1.5)]
    high = [i[0] for i in stations_level_over_threshold(stations,1.0)]
    moderate = [i[0] for i in stations_level_over_threshold(stations,0.8)]

    #build lists of towns of different level. 
    severe_town = []
    high_town = []
    moderate_town = []
    low_town = []
    for station in stations:
        if station.name in severe:
            if station.town not in severe_town:
                severe_town.append(station.town)
        elif station.name in high:
            if station.town not in high_town:
                high_town.append(station.town)
        elif station.name in moderate:
            if station.town not in moderate_town:
                moderate_town.append(station.town)
        elif type(MonitoringStation.relative_water_level(station)) == float: #to check the relative water level is valid
            if station.town not in low_town:
                low_town.append(station.town)
    
    severe_town.remove(None)
    high_town.remove(None)
    moderate_town.remove(None)
    low_town.remove(None)
    
    #print the lists
    for i in severe_town:
        print(i + ' is at severe risk.')
    for i in high_town:
        print(i + ' is at high risk.')
    for i in moderate_town:
        print(i + ' is at moderate risk.')
    for i in low_town:
        print(i + ' is at low risk.')


if __name__ == "__main__":
    run()