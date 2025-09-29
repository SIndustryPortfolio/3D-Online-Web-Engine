# MODULES
# INTERNAL
from forms.registerForm import RegisterForm

from modules.database import databaseCluster
from modules.userHandler import UserHandler
from modules.utilities import Utilities
from modules.shortcuts import Shortcuts

from modules.google.recaptcha import Recaptcha

# EXTERNAL
import time
import requests
import json
from flask import Blueprint, session, render_template, request, redirect, url_for, jsonify

# CORE
registerBlueprint = Blueprint("register", __name__)
secureInfo = Utilities.loadJson("secure/json/secure.json")


# Functions
# MECHANICS


#  Routes
@registerBlueprint.route("/register")
def pageHandler():
    # IF USER ALREADY LOGGED IN
    if session.get("user", None):
        return redirect(url_for("index.pageHandler"))
    
    siteKey = secureInfo["google"]["recaptcha"]["siteKey"]

    form = RegisterForm()
    return Shortcuts.renderPage("register.html", "Register", form=form, siteKey=siteKey)

    

@registerBlueprint.route("/registerRequest", methods = ["POST"]) # AJAX
def registerRequestPageHandler():
    # IF ALREADY LOGGED IN
    if session.get("user", None):
        return redirect(url_for("index.pageHandler"))
    
    # CORE
    response = {
        "status": "failed",
        "redirect" : None
    }

    data = request.get_json()
    requestIP = Shortcuts.getClientIP()

    # GOOGLE VERIFY
    googleRecaptchaResponse = Recaptcha.verifyForm(data)

    # IF USER NOT A BOT
    if not googleRecaptchaResponse["success"]:
        response["status"] = "failed"
        response["alert"] = googleRecaptchaResponse["alert"]
        return jsonify(response)

    username = data.get("username")
    email = data.get("email")

    password = data.get("password")

    # Functions
    # INIT        
    registerUserResponse = UserHandler.registerUser(username, email, password, requestIP)
    response["alert"] = registerUserResponse["alert"]

    # IF FAILED TO REGISTER
    if not registerUserResponse["success"]:
        return jsonify(response) 


    # IF REGISTER SUCCESSFUL
    user = UserHandler.getUserFromAttribute("username", username, caseSensitive=False)

    loginResponse = UserHandler.loginToUser(user.userId)

    #session["user"] = requests.get(request.host_url + "/api/v1/users/" + str(user.userId)).json() # API CALL FOR USER DATA

    if loginResponse["success"]:
        response["status"] = "success"
    else:
        response["status"] = "failed"
        
    response["alert"] = loginResponse["alert"]
    response["redirect"] = url_for("index.pageHandler")

    return jsonify(response) 

