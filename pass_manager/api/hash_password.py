import os
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from django.conf import settings


path = os.path.dirname(__file__)

def hash(string):
    data = string.encode('utf-8')
    data = base64.b64encode(data)
    public_key = RSA.importKey(open(path + "/.receiver.pem").read())
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encoded = cipher_rsa.encrypt(data)
    encoded = str(base64.b64encode(encoded))[2:-1]
    return encoded

def unhash(string):
    data = base64.b64decode(string)
    private_key = RSA.importKey(open(path + "/.private.pem").read())
    cipher_rsa = PKCS1_OAEP.new(private_key)
    data = cipher_rsa.decrypt(data)
    data = str(base64.b64decode(data))[2:-1]
    return data
