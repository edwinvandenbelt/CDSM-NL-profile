from admin.vehicle_import_controller import VehicleImportController
from admin.status_import_controller import VehicleStatusImportController
from admin.area_import_controller import AreaImportController
from admin.trip_import_controller import TripImportController

class ImportController():

    vehicle_import_controller: VehicleImportController = VehicleImportController()
    status_import_controller: VehicleStatusImportController = VehicleStatusImportController()
    area_import_controller: AreaImportController = AreaImportController()
    trip_import_controller: TripImportController = TripImportController()
    
    def import_all(self):
        report = {
            'vehicles': 'ok',
            'vehicle_status': 'ok',
            'area': 'ok',
            'trips': 'ok'
        }
        
        report['vehicles' ] = self.vehicle_import_controller.import_vehicles() 
        report['vehicle_status' ] = self.status_import_controller.import_vehicle_statusses()
        report['area'] = self.area_import_controller.import_area()
        report['trips'] = self.trip_import_controller.import_trip()

        return report

    def import_vehicles(self):
        return self.vehicle_import_controller.import_vehicles()
    
    def import_statusses(self):
        return self.status_import_controller.import_vehicle_statusses()
    
    def import_areas(self):
        return self.area_import_controller.import_area()
    
    def import_trip(self):
        return self.trip_import_controller.import_trip()