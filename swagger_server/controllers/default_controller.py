import connexion
from flask import abort, Response
from werkzeug.exceptions import HTTPException
from datetime import datetime

from swagger_server.models.iso_dayhour import IsoDayhour
from admin.vehicle_import_controller import VehicleImportController
from admin.status_import_controller import VehicleStatusImportController
from admin.area_import_controller import AreaImportController
from admin.trip_import_controller import TripImportController

def geofencing_zones_get():  # noqa: E501

    if 'token_info' not in connexion.context:
        return {}

    payload = connexion.context['token_info']
    if payload == None:
        return {}
    elif payload['municipality'] in AreaImportController.area_json:
        
        municipality = payload['municipality']
        if municipality in AreaImportController.area_json:
            return AreaImportController.area_json[municipality]
    
    return {} 


def trips_end_time_get(end_time):  # noqa: E501

    if 'token_info' not in connexion.context:
        return {}

    payload = connexion.context['token_info']
    if payload == None:
        return {}
    elif payload['municipality'] in TripImportController.trip_json:

        now = datetime.now().strftime("%Y-%m-%dT%H")

        if end_time > now:
            return "end_time is in the future", 404
        elif TripImportController.last_time < end_time:
            return "Data is not yet available", 202
        
        municipality = payload['municipality']
        if municipality in TripImportController.trip_json:
            if end_time in TripImportController.trip_json[municipality]:
                return TripImportController.trip_json[municipality][end_time]
            else:
                return "Provider wasn't in operation on this hour (end_time)", 404
    
    return {} 

def vehicles_get():  # noqa: E501

    if 'token_info' not in connexion.context:
        return {}

    payload = connexion.context['token_info']
    if payload == None:
        return {}
    elif payload['municipality'] in VehicleImportController.vehicle_json:
        
        municipality = payload['municipality']
        if municipality in VehicleImportController.vehicle_json:
            return VehicleImportController.vehicle_json[municipality]
    
    return {} 

def vehicles_status_get():  # noqa: E501
    
    if 'token_info' not in connexion.context:
        return {}

    payload = connexion.context['token_info']
    if payload == None:
        return {}
    elif payload['municipality'] in VehicleStatusImportController.status_json:
        
        municipality = payload['municipality']
        if municipality in VehicleStatusImportController.status_json:
            return VehicleStatusImportController.status_json[municipality]
    
    return {} 