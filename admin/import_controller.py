import json
from support.config_util import ConfigUtil as config
from swagger_server.models.vehicles import Vehicles
from swagger_server.models.vehicle import Vehicle

from time import time

class ImportController():

    vehicle_json : dict = {}
    
    def import_all(self):
        report = self.import_vehicles()
        return report

    def import_vehicles(self):
        self.read_vehicle_file()
        return json.loads( '{ "vehicles": "ok" }' )

    def read_vehicle_file(self):
        file = config.read_config_value('filename_vehicles')
        self.read_all(file)

    def read_all(self, file):
        new_vehicles: dict() = {}

        try:
            with open(file, "r") as csv_file:
                lines = csv_file.readlines()
                for line in lines:
                    vehicle, municipality = self.convert_to_vehicle(line)

                    if municipality not in new_vehicles:
                       new_vehicles[municipality] = Vehicles(version="2.0", vehicles=list())

                    new_vehicles[municipality].vehicles.append(vehicle)

            ImportController.vehicle_json = new_vehicles
        except Exception as e:
            print("An exception occurred:", e)
            raise e

    def convert_to_vehicle(self,line):
        # 004c9d6f-7523-461a-b6e7-946dbf13fda6;dadcd6bf-3ab5-4c2d-8609-23a92f1a4672;TXXT95;car;combustion;280000;0;130;markelo
        parts = line.split(';')

        vehicle = Vehicle()
        vehicle.device_id = parts[0] 
        vehicle.provider_id = parts[1]
        vehicle.vehicle_id = parts[2]
        vehicle.vehicle_type = parts[3]
        vehicle.propulsion_types = parts[4].split(',')
        
        if int(parts[5]) > 0:
            vehicle.battery_capacity = int(parts[5])
        if int(parts[6]) > 0:
            vehicle.fuel_capacity = parts[6]
        if int(parts[7]) > 0:
            vehicle.maximum_speed = parts[7]
        
        return vehicle, parts[8].strip()
    
