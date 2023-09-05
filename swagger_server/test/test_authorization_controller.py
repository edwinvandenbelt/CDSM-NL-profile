import unittest
from controllers.authorization_controller import check_bearer
from unittest.mock import patch

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