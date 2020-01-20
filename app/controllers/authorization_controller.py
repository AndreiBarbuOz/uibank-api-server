from typing import List
import jwt
from app import auth

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html
"""
def check_bearerAuth(token):
    #raise Exception("see stack")
    return auth.decode_token(token)


