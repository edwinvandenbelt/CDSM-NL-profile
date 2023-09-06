from admin.vehicle_import_controller import VehicleImportController
from admin.status_import_controller import VehicleStatusImportController

class ImportController():

    vehicle_import_controller: VehicleImportController = VehicleImportController()
    status_import_controller: VehicleStatusImportController = VehicleStatusImportController()
    
    def import_all(self):
        report = {
            'vehicles': 'ok',
            'vehicle_status': 'ok'
        }
        
        report['vehicles' ] = self.vehicle_import_controller.import_vehicles() 
        report['vehicle_status' ] = self.status_import_controller.import_vehicle_statusses()
        return report
