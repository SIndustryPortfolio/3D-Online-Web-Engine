#
class User:
    def __init__(self, userId, username, userType, email, emailVerified, registerTime, lastLoginTime, IP):
        self.userId = userId
        self.username = username
        self.userType = userType
        self.email = email
        self.emailVerified = emailVerified
        self.registerTime = registerTime
        self.lastLoginTime = lastLoginTime
        self.IP = IP

    def getDict(self):
        return {
            "userId": self.userId,
            "username": self.username,
            "email": self.email,
            "emailVerified": self.emailVerified,
            "registerTime": self.registerTime,
            "lastLoginTime": self.lastLoginTime,
            "IP": self.IP
        }