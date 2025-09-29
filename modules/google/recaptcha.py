# MODULES
# EXT
import requests

# CORE
recaptchaVerifyURL = "https://www.google.com/recaptcha/api/siteverify"
recaptchaSecretKey = "6LcAIdAqAAAAAJr5K8R2CTI8Edj9_LSnZjCfDO1P"

class Recaptcha:
    def verifyForm(formDict): # CHECK IF FORM WAS COMPLETED BY HUMAN
        # CORE
        response = {"success": True, "alert": {"type": "danger", "message": ""}}

        secretResponse = formDict["g-recaptcha-response"]
        verifyResponse = requests.post(url=f'{recaptchaVerifyURL}?secret={recaptchaSecretKey}&response={secretResponse}').json()

        if not verifyResponse["success"] or verifyResponse["score"] < 0.5:
            response["success"] = False
            response["alert"]["type"] = "danger"
            response["alert"]["message"] = "Failed google recaptcha"
            return response
        
        response["success"] = True
        response["alert"]["type"] = "success"
        response["alert"]["message"] = "successfully passed google recaptcha"

        return response

