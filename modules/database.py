# Modules
# INT
from modules.utilities import Utilities

# EXT
import json
from pymongo import MongoClient

# CORE
#coreInfo = Utilities.loadJson("static/json/core.json")

secureInfo = Utilities.loadJson("secure/json/secure.json")


client = MongoClient("mongodb+srv://" + secureInfo["dbAuth"]["username"] + ":" + secureInfo["dbAuth"]["secretKey"] + "@dissertationcluster.so7tm.mongodb.net/?retryWrites=true&w=majority&appName=dissertationCluster")
databaseCluster = client["dissertationDatabase"]

# 
class Database:
    def getAndUpdateCounter(collectionName): # FOR NUMBER BASED IDs ON RECORDS
        counterCollection = databaseCluster["counter"]

        document = counterCollection.find_one_and_update( 
            {"collection": collectionName},
            {"$inc": {"count": 1}},
            upsert = True,
            return_document = True
        )

        return document["count"]