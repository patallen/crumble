from Crypto.Cypher import AES
from app import app

encryptor = AES.new(app.config.get('SECRET_KEY'))


def encrypt(string):
    return encryptor.encrypt(string)


def decrypt(string):
    return encryptor.decrypt(string)
