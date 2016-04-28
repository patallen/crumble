from Crypto.Cipher import AES
from Crypto import Random
from app import app

iv = Random.new().read(AES.block_size)
encryptor = AES.new(app.config.get('SECRET_KEY'), AES.MODE_CBC, iv)


def encrypt(string):
    return encryptor.encrypt(string)


def decrypt(string):
    return encryptor.decrypt(string)
