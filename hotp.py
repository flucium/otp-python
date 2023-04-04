import hmac
import hashlib

def hotp(secret,digits,counter):
        
    hmac_result = hmac.new(secret,counter.to_bytes(8,"big"),hashlib.sha1).digest()

    offset = hmac_result[19] & 0x0f

    bin_code = bin( (hmac_result[offset]  & 0x7f) << 24 | (hmac_result[offset+1] & 0xff) << 16 | (hmac_result[offset+2] & 0xff) <<  8 | (hmac_result[offset+3] & 0xff))

    snum = int(bin_code,2)
        
    return snum % 10**digits