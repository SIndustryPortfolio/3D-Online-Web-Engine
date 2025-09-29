# MODULES
# INTERNAL
from modules.utilities import Utilities
from modules.shortcuts import Shortcuts

from controllers.worldController import servers

# EXTERNAL
import requests
import json
from flask import Blueprint, session, render_template, request, redirect, url_for, jsonify

# CORE
gameBlueprint = Blueprint("game", __name__)


# MECHANICS

#  Routes
@gameBlueprint.route("/game/<int:_serverId>")
def pageHandler(_serverId):
    # Functions
    # INIT
    user = session.get("user", None)

    if not user: # IF USER NOT LOGGED IN
        return redirect(url_for("login.pageHandler"))
    
    if not str(_serverId) in servers: # IF SERVER DOESN'T EXIST
        return redirect(url_for("index.pageHandler"))
    

    server = servers[str(_serverId)]

    # MAP RAW GRID DATA
    mapData = requests.get(request.host_url + "/api/v1/game/maps/" + server.map).json()
    
    # TEXTURE RGB DATA
    textures = requests.get(request.host_url + "/api/v1/game/textures/raw").json()

    # MAP META DATA (TRANSLATE GRID TO RENDERABLE INFORMATION)
    mapMeta = requests.get(request.host_url + "/api/v1/game/maps/meta").json()

    return Shortcuts.renderPage("game.html", "Game", serverId=str(_serverId), mapData=mapData, textures=textures, mapMeta=mapMeta)

