import hotp
import datetime

def totp(secret,digits):
    x = 30
    
    t = (datetime.datetime.utcnow() - datetime.datetime(1970,1,1,0,0)).total_seconds()

    t = int(t / x)

    return hotp(secret,digits,t)


# provided = "EXAMPLE"

# user = "user@example.com"

# secret = base64.b32encode(b"secret key").upper().decode()

# issuer = "ISSUER"

# algorithm = "SHA1"

# digits = 6

# period = 30

# uri = "otpauth://totp/{}:{}?secret={}&issuer={}&algorithm={}&digits={}&period={}".format(provided,user,secret,issuer,algorithm,digits,period)

# print(uri)