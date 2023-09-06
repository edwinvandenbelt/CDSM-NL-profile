from admin.vehicle_import_controller import VehicleImportController
from admin.status_import_controller import VehicleStatusImportController
from admin.area_import_controller import AreaImportController

class ImportController():

    vehicle_import_controller: VehicleImportController = VehicleImportController()
    status_import_controller: VehicleStatusImportController = VehicleStatusImportController()
    area_import_controller: AreaImportController = AreaImportController()
    
    def import_all(self):
        report = {
            'vehicles': 'ok',
            'vehicle_status': 'ok',
            'area': 'ok'
        }
        
        report['vehicles' ] = self.vehicle_import_controller.import_vehicles() 
        report['vehicle_status' ] = self.status_import_controller.import_vehicle_statusses()
        report['area'] = self.area_import_controller.import_area()
        return report
