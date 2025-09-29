# Modules
# EXT
import time

# INT
from modules.userHandler import UserHandler

# CORE
cache = {}

class UserServiceCache:
    def remove(userId):
        # Functions
        # INIT
        cache.pop(userId)

    def getAll():
        # Functions
        # INIT
        return cache

    def update(userId):
        # Functions
        # INIT
        UserServiceCache.set(userId, UserServiceCache.get(userId))

    def get(userId):
        # Functions
        # INIT
        if not userId in cache:
            user = UserHandler.getUserFromUserId(userId)

            if user != None:
                UserServiceCache.set(userId, user.getDict())
                
        return cache[userId]["value"]

    def set(userId, value):
        # CORE
        timeNow = time.time()

        # Functions
        # INIT
        cache[userId] = {"value": value, "time": timeNow}