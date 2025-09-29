# Modules
# EXT
import time
import os

# INT
from modules.utilities import Utilities
from flask import current_app

# CORE
cache = {}

class MapServiceCache:
    def remove(mapName):
        # Functions
        # INIT
        cache.pop(mapName)

    def getAll():
        # Functions
        # INIT
        mapsDirectory = os.path.join(current_app.root_path, "static", "json", "maps")
        filesInDirectory = os.listdir(mapsDirectory)

        for file in os.listdir(mapsDirectory):
                fullPath = os.path.join(mapsDirectory, file)
                fileBaseName = os.path.splitext(os.path.basename(fullPath))[0]
                if os.path.isfile(fullPath):
                    MapServiceCache.get(fileBaseName)
           
        return cache

    def get(mapName):
        # Functions
        # INIT
        if not mapName in cache:
            MapServiceCache.set(mapName, Utilities.loadJson("static/json/maps/" + mapName + ".json"))

        return cache[mapName]["value"]

    def set(mapName, value):
        # CORE
        timeNow = time.time()

        # Functions
        # INIT
        cache[mapName] = {"value": value, "time": timeNow}