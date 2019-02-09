import base64
import os
import hashlib

db = {}

salt = base64.b64encode(os.urandom(32))


def get_digest(password):
    digest = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), salt, 10000)
    return digest


def is_login(user_name, password):
    return get_digest(password) == db[user_name]


db['user1'] = get_digest('password1')

print(is_login('user1', 'password1'))
