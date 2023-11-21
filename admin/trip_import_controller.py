import os

from datetime import date, timedelta
from support.config_util import ConfigUtil as config
from swagger_server.models.trip import Trip
from swagger_server.models.trips import Trips
from swagger_server.models.gps import Gps

class TripImportController():

    trip_json : dict = {}
    last_time = ""
    
    def import_trip(self):
        files_processed, errors = self.read_trip_files()
        return { 'status': 'ok', 'files_processed': files_processed, 'errors': errors }

    def read_trip_files(self):
        dir = config.read_config_value('directoryname_trips')
        errors = dict()
        files_processed = []
        for file in os.listdir(dir):
            if file.startswith("trip") and file.endswith( ".csv"):
                errors[file] = self.read_all(dir, file)
                files_processed.append(file)
        
        return files_processed, errors

    def read_all(self, dir, file):
        errors = []
        try:
            provider_id = config.read_config_value('provider_id')

            with open(dir + file, "r") as csv_file:
                file_parts = file.split('.') # trips.YYYY-MM-DDTHH.csv
                time = file_parts[1]
                lines = csv_file.readlines()
                for line in lines:
                    if line != None and line != "" and not line.startswith("device_id"):    
                        municipality, trip, found_errors = self.convert_to_trip(line)
                        trip.provider_id = provider_id

                        if found_errors != None:
                            errors.append(found_errors)

                        else:                        
                            if municipality not in self.trip_json:
                                TripImportController.trip_json[municipality] = {}

                            if time not in self.trip_json[municipality]:  
                                TripImportController.trip_json[municipality][time] = Trips(trips=list(), version="2.0")

                            TripImportController.trip_json[municipality][time].trips.append(trip)

            if TripImportController.last_time == "" or TripImportController.last_time < time:
                TripImportController.last_time = time

        except Exception as e:
            print("An exception occurred:", e)
            raise e
        
        return errors

    def convert_to_trip(self,line):
        try:
            # device_id;trip_id;start_time;end_time;start_location;end_location;duration;distance;municipality
            parts = line.split(';')

            trip = Trip()
            trip.device_id = parts[0] 
            trip.trip_id = parts[1]
            trip.start_time = int(parts[2])
            trip.end_time = int(parts[3])
            trip.start_location = self.to_gps(parts[4])
            trip.end_location = self.to_gps(parts[5])
            trip.duration = int(parts[6])
            trip.distance = int(parts[7])

            return parts[8].strip(), trip, None
        except Exception as e:
            return None, None, str(e) + ' line: ' + line
    
    def to_gps(self, part):
        gps = part.split(',')
        return Gps(lat=float(gps[0]), lng=float(gps[1]))
    
    def remove_old_entries(self, days):

        limit = date.today() - timedelta(days=days)
        limit = limit.strftime("%Y-%m-%dT%H")

        for municipality in self.trip_json:
            to_clear = list()
            for hour in self.trip_json[municipality]:
                if hour < limit:
                    to_clear.append(hour)

            for hour in to_clear:
                self.trip_json[municipality].pop(hour)
        
