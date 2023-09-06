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
            with open(file, "r") as csv_file:
                lines = csv_file.readlines()
                for line in lines:
                    if line != None and line != "":
                        vehicle_status, municipality = self.convert_to_vehicle_status(line)

                        if municipality not in new_statusses:
                            new_statusses[municipality] = Statusses(version="2.0", vehicles_status=list())

                        new_statusses[municipality].vehicles_status.append(vehicle_status)

            VehicleStatusImportController.status_json = new_statusses
        except Exception as e:
            print("An exception occurred:", e)
            raise e

    def convert_to_vehicle_status(self,line):

        parts = line.split(';')
        # device_id;provider_id;event_id;vehicle_state;event_types;timestamp;location;battery_percent;fuel_percent;telemetry_id;timestamp;trip_ids;journey_id;location;municipality

        status = Status()
        status.device_id = parts[0] 
        status.provider_id = parts[1]
       
        status.last_event = self.convert_to_event(parts)
        status.last_telemetry = self.convert_to_telemetry(parts)
        
        return status, parts[14].strip()
    
    def convert_to_event(self, parts):
        event = Event()
        event.device_id = parts[0]
        event.provider_id = parts[1]
        event.event_id = parts[2]
        event.vehicle_state = parts[3]
        event.event_types = parts[4].split(',')
        event.timestamp = int(parts[5])
        event.location = self.to_gps(parts[6])
        if int(parts[7]) > 0:
            event.battery_percent = int(parts[7])
        if int(parts[8]) > 0:
            event.fuel_percent = int(parts[8])
        return event

    def convert_to_telemetry(self, parts):
        telemetry = Telemetry()
        telemetry.device_id = parts[0]
        telemetry.provider_id = parts[1]
        telemetry.telemetry_id = parts[9]
        telemetry.timestamp = int(parts[10])
        #telemetry.trip_ids = None
        #telemetry.journey_id = None
        telemetry.location = self.to_gps(parts[13])
        return telemetry
    
    def to_gps(self, part):
        gps = part.split(',')
        return Gps(lat=float(gps[0]), lng=float(gps[1]))
