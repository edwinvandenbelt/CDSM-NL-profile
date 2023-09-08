from admin.import_controller import ImportController
from support.config_util import ConfigUtil as config

class ClearController():

    container: ImportController

    def __init__(self, data_container: ImportController):
        self.container = data_container

    def clear(self):
        days = int(config.read_config_value('trip_retention_days'))
        self.container.trip_import_controller.remove_old_entries(days)
        return { 'status': 'ok' }