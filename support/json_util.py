import json

class JsonUtil:
    
    @staticmethod
    def read_all_json(json_file_name):
        try:
            with open(json_file_name, "r") as json_file:
                return json.load(json_file)
        except Exception as e:
            print("An exception occurred:", e)
            raise e
