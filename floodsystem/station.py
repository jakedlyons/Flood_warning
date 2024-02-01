# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def typical_range_consistent(self):
        if self.typical_range == None: # if data is missing
            return False
        elif self.typical_range[1] < self.typical_range[0]: #typical high is less than typical low
            return False
        else: #consistent, consider case typical_high = typical_low as consistent
            return True

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

def inconsistent_typical_range_stations(stations):
    inconsistent_typical_range_stations = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) is False:
            inconsistent_typical_range_stations.append(station.name)
        else:
            pass
    return inconsistent_typical_range_stations