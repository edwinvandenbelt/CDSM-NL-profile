import jwt
from support.config_util import ConfigUtil as config

class JwtUtil:

    @staticmethod
    def decrypt(token: str):
        secret = config.read_config_value('jwt_secret')
        decoded_data = jwt.decode(jwt=token,
                                key=secret,
                                algorithms=["HS256"])
        return decoded_data