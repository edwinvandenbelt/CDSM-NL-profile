import connexion

from swagger_server.models.iso_dayhour import IsoDayhour
from admin.vehicle_import_controller import VehicleImportController
from admin.status_import_controller import VehicleStatusImportController


def geofencing_zones_get():  # noqa: E501
    """return the operational area, according to the shared mobility provider

    The provider must offer the GBFS /geofencing_zones.json file (https://github.com/MobilityData/gbfs/blob/v2.3/gbfs.md#geofencing_zonesjson). # noqa: E501


    :rtype: GeofencingZones
    """
    return 'do some magic!'


def trips_end_time_get(end_time):  # noqa: E501
    """Query historical trip data.

    Get all trips with an end time occurring within the hour. # noqa: E501

    :param end_time: A list of the languages/localizations the user would like to see the results in. For user privacy and ease of use on the TO side, this list should be kept as short as possible, ideally just one language tag from the list in operator/information
    :type end_time: dict | bytes

    :rtype: Trips
    """
    if connexion.request.is_json:
        end_time = IsoDayhour.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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