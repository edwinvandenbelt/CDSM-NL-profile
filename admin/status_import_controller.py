import json
from support.config_util import ConfigUtil as config
from swagger_server.models.statusses import Statusses, Status
from swagger_server.models.event import Event
from swagger_server.models.telemetry import Telemetry
from swagger_server.models.gps import Gps

class VehicleStatusImportController():

    status_json : dict = {}
    
    def import_vehicle_statusses(self):
        self.read_vehicle_status_file()
        return "ok"

    def read_vehicle_status_file(self):
        file = config.read_config_value('filename_vehicle_status')
        self.read_all(file)

    def read_all(self, file):
        new_statusses: dict() = {}

        try:
            provider_id = config.read_config_value('provider_id')
            with open(file, "r") as csv_file:
                lines = csv_file.readlines()
                for line in lines:
                    if line != None and line != "" and not line.startswith("device_id"):
                        vehicle_status, municipality = self.convert_to_vehicle_status(line, provider_id)

                        if municipality not in new_statusses:
                            new_statusses[municipality] = Statusses(version="2.0", vehicles_status=list())

                        new_statusses[municipality].vehicles_status.append(vehicle_status)

            VehicleStatusImportController.status_json = new_statusses
        except Exception as e:
            print("An exception occurred:", e)
            raise e

    def convert_to_vehicle_status(self,line,provider_id):

        parts = line.split(';')
        # device_id;event_id;vehicle_status;timestamp;location;municipality

        status = Status()
        status.device_id = parts[0] 
        status.provider_id = provider_id
       
        status.last_event = self.convert_to_event(parts, provider_id)
        status.last_telemetry = self.convert_to_telemetry(parts, provider_id)
        
        return status, parts[5].strip()
    
    def convert_to_event(self, parts, provider_id):
        
        # device_id;event_id;vehicle_status;timestamp;location;municipality
        event = Event()
        event.device_id = parts[0]
        event.provider_id = provider_id
        event.event_id = parts[1]
        event.vehicle_state = parts[2]
        event.timestamp = int(parts[3])
        event.location = self.to_gps(parts[4])
        return event

    def convert_to_telemetry(self, parts, provider_id):
        telemetry = Telemetry()
        telemetry.device_id = parts[0]
        telemetry.provider_id = provider_id
        telemetry.telemetry_id = parts[1]
        telemetry.timestamp = int(parts[3])
        telemetry.location = self.to_gps(parts[4])
        return telemetry
    
    def to_gps(self, part):
        gps = part.split(',')
        return Gps(lat=float(gps[0]), lng=float(gps[1]))
