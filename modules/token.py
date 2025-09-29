# MODULES
import random
import string

# CORE
length = 32

#
class Token:
    def generate(): # GENERATE RANDOM STRING OF CHARACTERS TO REPRESENT A TOKEN
        # CORE
        digits = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase

        # Functions
        # INIT
        tokenString = ""

        for x in range(0, length - 1):
            tokenString += random.choice(digits)

        return tokenString