# MODULES
# INT
from modules.discordBot import DiscordBot

# EXT
from datetime import datetime

###
class Debug:

    def logError(exception, startFormattedTime, endFormattedTime):
        # Functions
        # INIT

        # DISCORD WEB HOOK EMBED MESSAGE
        messageEmbed = {
            "title": "Error Caught!",
            "description": "",
            "color": 0xff0000,
            "fields": [
                {
                    "name": "Start Time: " + str(startFormattedTime) + " | End Time: " + str(endFormattedTime),
                    "value": str(exception)
                },
            ]
        }

        packagedToSend = {
            "content": "",
            "embeds": [messageEmbed]
        }

        botResponse = DiscordBot.send("errors", packagedToSend)

    def pcall(method, *args): # TRY CATCH WITH DEBUG LOG TO DISCORD
        # CORE
        formattedStartTime = datetime.now().strftime("%H:%M")
        error = None

        success = False
        response = None

        # Functions
        # INIT
        try:
            response = method(*args)
            success = True
        except (KeyboardInterrupt, SystemExit): # NO POINTLESS LOG ON SHUTDOWN
            pass
        except Exception as e:
            success = False
            response = None
            
            error = e

        formattedEndTime = datetime.now().strftime("%H:%M")

        if not success:
            Debug.logError(error, formattedStartTime, formattedEndTime)

        return success, response