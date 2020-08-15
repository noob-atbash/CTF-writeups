from Crypto.Cipher import DES
import base64
from FLAG import flag


def pad(plaintext):
    while len(plaintext) % 8 != 0:
        plaintext += "*"
    return plaintext

def enc(plaintext,key):
    cipher = DES.new(key, DES.MODE_ECB)
    return base64.b64encode(cipher.encrypt(plaintext))


key = "##############".decode("hex")
plaintext = pad(flag)
print enc(plaintext,key)