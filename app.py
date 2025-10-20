# MODULES

# EXT
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, render_template, url_for
from flask_socketio import SocketIO
from flask_mail import Mail
from flask_wtf import recaptcha
from flask_wtf.csrf import CSRFProtect

# INT
from modules.google.recaptcha import Recaptcha, recaptchaSecretKey
from modules.utilities import Utilities
from modules.debug import Debug



# CORE
coreInfo = Utilities.loadJson("static/json/core.json")
secureInfo = Utilities.loadJson("secure/json/secure.json")

scheduler = BackgroundScheduler()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config["RECAPTCHA_PUBLIC_KEY"] = secureInfo["google"]["recaptcha"]["siteKey"]
app.config["RECAPTCHA_PRIVATE_KEY"] =  recaptchaSecretKey
#
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_PASSWORD"] = secureInfo["google"]["email"]["appPassword"]
app.config["MAIL_USERNAME"] = secureInfo["google"]["email"]["address"]
app.config["MAIL_DEFAULT_SENDER"] = secureInfo["google"]["email"]["address"]
#

mail = Mail(app)
csrf = CSRFProtect(app)
socketIO = SocketIO(app)

# CONTROLLERS
from controllers.api.apiV1 import apiV1Blueprint
from controllers.worldController import socketIO, worldControllerInitialise
from controllers.indexController import indexBlueprint
from controllers.homeController import homeBlueprint
from controllers.loginController import loginBlueprint
from controllers.registerController import registerBlueprint
from controllers.settingsController import settingsBlueprint
from controllers.gameController import gameBlueprint
from controllers.multiFactorAuthenticationController import multiFactorAuthenticationBlueprint

# Functions
# MECHANICS
def initialise():
    # Functions
    # INIT
    scheduler.start()
    socketIO.run(app, host='0.0.0.0', port=5000, debug=True)

def end():
    # Functions
    # INIT
    scheduler.shutdown()

with app.app_context():
    # Functions
    # INIT
    worldControllerInitialise()

# INIT
app.register_blueprint(apiV1Blueprint, url_prefix="/api/v1")

app.register_blueprint(indexBlueprint)
app.register_blueprint(homeBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(multiFactorAuthenticationBlueprint)
app.register_blueprint(registerBlueprint)
app.register_blueprint(settingsBlueprint)
app.register_blueprint(gameBlueprint)

if __name__ == "__main__":
    success, response = Debug.pcall(initialise)
    end()

    #try:
    #    scheduler.start()
    #    socketIO.run(app, debug=True)
    #except (KeyboardInterrupt, SystemExit):
    #    pass
    #finally:
    #    scheduler.shutdown()