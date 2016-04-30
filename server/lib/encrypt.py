from Crypto.Cipher import AES
from Crypto import Random
from app import app

iv = 'thisiskdjiejfisn'
encryptor = AES.new(app.config.get('SECRET_KEY'), AES.MODE_CBC, iv)


def pad(string, block_size=16):
    to_pad = block_size - ((block_size + len(string)) % block_size)
    digits = len(str(to_pad))

    zeros = block_size + to_pad - digits
    return "{0}{1}".format(string, ("{}{}".format('0'*zeros, str(to_pad))))


def unpad(string, block_size=16):
    num = int(string[-2:len(string)]) + 16
    return string[:-num]


def encrypt(string):
    return encryptor.encrypt(string)


def decrypt(string):
    return encryptor.decrypt(string)
