from support.json_util import JsonUtil as jsonutil
import os

class ConfigUtil:    

    @staticmethod
    def read_config_value(key_name):
        value = os.getenv(key_name)
        if value != None:
            return value

        try:
            json_file_path = './config/config.json'
            if not os.path.exists(json_file_path):
                print("file does not exist: " + os.getcwd() + json_file_path)
            config = jsonutil.read_all_json(json_file_path)

            for key,value in config.items():
                if key == key_name:
                    return value
            
        except Exception as e:
            print("An exception occurred:", e, flush=True)
            raise e