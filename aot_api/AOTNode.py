from datetime import datetime, timedelta # allows me to cache data

import sqlite3
from sqlite3 import Error

import logging

from itertools import count

# Database that caches node data and properties for each loop
class AOTDataCache:

    def __init__(self):
        try:
            self.__sqliteDBInstance = sqlite3.connect(":memory:")
            logging.info("Created Internal SQLite3 service in RAM.")
        except Error as e:
            logging.error("Could not initialize SQLite 3 instance. Received Error: " + str(e))
            exit(-1)
        finally:
            if self.__sqliteDBInstance != None:
                self.__sqliteDBInstance.close()

    def __del__(self):
        self.__sqliteDBInstance.close()

    # returns a python dictionary that has the following format:
        # {
        #   'address': str(), # a human readable street address or TBD for temporary placement
        #   'description': str(), # A description of the AOT device. Ex: AoT Chicago (S) [C]
        #   'location': geojson() # a geojson point object that refers to the specific location that thing is on.
        # }
    def getNodeData(self, vsn : str):
        pass

    # returns a list of the most recent measurement from each sensor.
    # Returns a dictionary with the following format:
        # {
        #    'timestamp': datetime(), # when the measurement was taken
        #    'data' : {
                    #   <sensor_path0>str() : {
                    #                           'value' : int/str/float/etc,
                    #                           'uom' : str()
                    #                        },
                    #   <sensor_path1>str() : {
                    #                           'value' : int/str/float/etc,
                    #                           'uom' : str()
                    #                        },
                    #           ....
                    #   <sensor_pathn>str() : {
                    #                           'value' : int/str/float/etc,
                    #                           'uom' : str()
                    #                        }
        #             }
        # }
    def getMostRecentNodeObservation(self, vsn : str):
        pass

    

# This class represents a node and it's data.
# It automatically constructs the data 
class AOTNode:

    default_cache = AOTDataCache()

    # will, give the vsn, produce a full AOTNode object with 
    def __init__(self, vsn : str, data_cache : AOTDataCache = AOTNode.default_cache):
        self.vsn = vsn

    # gets data either from cache (if it has been more than 5 minutes since last read) or from the internet
    def getData(self) -> dict:
        pass
