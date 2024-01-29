import unittest
from unittest.mock import patch
from swagger_server.controllers.authorization_controller import check_bearer

class TestAuthorizationController(unittest.TestCase):

    @unittest.expectedFailure
    def test_no_bearer(self):
        check_bearer(None)

    @unittest.expectedFailure
    def test_invalid_bearer(self):
        check_bearer('333')

    def test_valid_bearer(self):
        with patch('support.config_util.ConfigUtil.read_config_value') as mock_config:
            mock_config.side_effect = ["vianova", "[Vianova]"]

            config = check_bearer('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVmlhbm92YSJ9.MPTve5whDIK95QtRU6AicRBCwELV1aFSiAL9X2Ckcto')
        self.assertEquals('Vianova', config['municipality'])

    def test_unrevoked_id(self):
        with patch('support.config_util.ConfigUtil.read_config_value') as mock_config:
            mock_config.side_effect = ["vianova", ["Vianova"], []]

            config = check_bearer('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlZpYW5vdmEiLCJpYXQiOjE1MTYyMzkwMjIsImlkIjoiMSJ9.Th5bTjeZubz9yp3IrPK_f6lQRYRoHXPQTEQQ5G5UzE0')
        self.assertEquals('Vianova', config['municipality'])

    def test_unrevoked_id_other_id_in_revoked_list(self):
        with patch('support.config_util.ConfigUtil.read_config_value') as mock_config:
            mock_config.side_effect = ["vianova", ["Vianova"], ["12"]]

            config = check_bearer('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlZpYW5vdmEiLCJpYXQiOjE1MTYyMzkwMjIsImlkIjoiMSJ9.Th5bTjeZubz9yp3IrPK_f6lQRYRoHXPQTEQQ5G5UzE0')
        self.assertEquals('Vianova', config['municipality'])

    @unittest.expectedFailure
    def test_revoked_id(self):
        with patch('support.config_util.ConfigUtil.read_config_value') as mock_config:
            mock_config.side_effect = ["vianova", ["Vianova"], ["1"]]

            check_bearer('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlZpYW5vdmEiLCJpYXQiOjE1MTYyMzkwMjIsImlkIjoiMSJ9.Th5bTjeZubz9yp3IrPK_f6lQRYRoHXPQTEQQ5G5UzE0')

    @unittest.expectedFailure
    def test_blocked_tokens_without_id_in_payload(self):
        with patch('support.config_util.ConfigUtil.read_config_value') as mock_config:
            mock_config.side_effect = ["vianova", ["Vianova"], ["1"]]

            check_bearer('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiVmlhbm92YSJ9.MPTve5whDIK95QtRU6AicRBCwELV1aFSiAL9X2Ckcto')
