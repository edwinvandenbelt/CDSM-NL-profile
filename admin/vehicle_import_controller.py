import json
from support.config_util import ConfigUtil as config
from swagger_server.models.vehicles import Vehicles
from swagger_server.models.vehicle import Vehicle

class VehicleImportController():

    vehicle_json : dict = {}
    
    def import_vehicles(self):
        self.read_vehicle_file()
        return 'ok'

    def read_vehicle_file(self):
        file = config.read_config_value('filename_vehicles')
        self.read_all(file)

    def read_all(self, file):
        new_vehicles: dict() = {}

        try:
            provider_id = config.read_config_value('provider_id')

            with open(file, "r") as csv_file:
                lines = csv_file.readlines()
                for line in lines:
                    if line != None and line != "" and not line.startswith("device_id"):
                        vehicle, municipality = self.convert_to_vehicle(line)
                        vehicle.provider_id = provider_id

                        if municipality not in new_vehicles:
                            new_vehicles[municipality] = Vehicles(version="2.0", vehicles=list())

                        new_vehicles[municipality].vehicles.append(vehicle)

            VehicleImportController.vehicle_json = new_vehicles
        except Exception as e:
            print("An exception occurred:", e)
            raise e

    def convert_to_vehicle(self,line):
        # device_id;vehicle_type;propulsion_type;municipality
        parts = line.split(';')

        vehicle = Vehicle()
        vehicle.device_id = parts[0] 
        vehicle.vehicle_id = parts[0]
        vehicle.vehicle_type = parts[1]
        vehicle.propulsion_types = parts[2].split(',')
        
        return vehicle, parts[3].strip()