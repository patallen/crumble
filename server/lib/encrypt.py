from Crypto.Cipher import AES
from Crypto import Random
from app import app

iv = Random.new().read(AES.block_size)
encryptor = AES.new(app.config.get('SECRET_KEY'), AES.MODE_CBC, iv)


def pad(string, block_size=16):
    to_pad = len(string) % block_size

    if to_pad >= 0:
        digits = 1
    if to_pad > 9:
        digits = 2

    zeros = block_size + to_pad - digits
    return "{0}{1}".format(string, ("{}{}".format('0'*zeros, str(to_pad))))


def encrypt(string):
    return encryptor.encrypt(pad(string))


def decrypt(string):
    return encryptor.decrypt(string)
