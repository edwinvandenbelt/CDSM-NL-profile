import json
from support.config_util import ConfigUtil as config

class AreaImportController():

    area_json : dict = {}
    
    def import_area(self):
        files = config.read_config_value('filenames_areas')

        for entry in files:
            self.area_json[entry['municipality']] = self.read_all(entry['file'])
        return 'ok'

    def read_all(self, file):
        new_json = ""

        try:
            with open(file, "r") as csv_file:
                new_json = csv_file.read()
                
        except Exception as e:
            print("An exception occurred:", e)
            raise e
        
        return json.loads(new_json)
