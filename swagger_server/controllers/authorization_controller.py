from support.jwt_util import JwtUtil
from flask import abort
from support.config_util import ConfigUtil as config

"""
controller generated to handled auth operation described at:
https://connexion.readthedocs.io/en/latest/security.html

Generate tokens using
https://jwt.io/#debugger-io
"""
def check_bearer(token):
    try:
        decrypted_token = JwtUtil.decrypt(token)

        if 'name' not in decrypted_token:
            abort(401)

        name = decrypted_token['name']
    except Exception as e:
        abort(401)

    allowed_tokens = config.read_config_value("allowed_tokens")
    if name in allowed_tokens:

        # if blocked tokens are applicable
        blocked_tokens = config.read_config_value('blocked_tokens')
        if blocked_tokens != None:
            if 'id' not in decrypted_token or decrypted_token['id'] in blocked_tokens:
                abort(401)

        return { "municipality" : name }

    abort(401)


