# MODULES
# INTERNAL
from modules.utilities import Utilities
from modules.shortcuts import Shortcuts

from controllers.worldController import servers

# EXTERNAL
import json
from flask import Blueprint, session, render_template, request, redirect, url_for, jsonify

# CORE
homeBlueprint = Blueprint("home", __name__)


#  Routes
@homeBlueprint.route("/home")
def pageHandler():
    # Functions
    # INIT
    if not session.get("user", None): # IF NOT USER LOGGED IN
        return redirect(url_for("login.pageHandler"))


    return Shortcuts.renderPage("home.html", "Home", servers = servers)

