import jwt
import time
import os

JWT_ISSUER = 'uibank.azurewebsites.com'
JWT_SECRET = os.environ['JWT_SECRET']
JWT_LIFETIME_SECONDS = 3600
JWT_ALGORITHM = 'HS256'

def generate_token(user_id, exp=None):
    timestamp = _current_timestamp()
    if exp is None:
        exp = int(timestamp + JWT_LIFETIME_SECONDS)
    payload = {
        "iss": JWT_ISSUER,
        "exp": exp,
        "sub": str(user_id),
    }
    ret = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return ret


def decode_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.exceptions.InvalidTokenError as e:
        print(e)
        pass


def _current_timestamp() -> int:
    return int(time.time())
