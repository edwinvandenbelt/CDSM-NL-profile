import connexion
import json

from swagger_server.models.geofencing_zones import GeofencingZones  # noqa: E501
from swagger_server.models.iso_dayhour import IsoDayhour  # noqa: E501
from swagger_server.models.statusses import Statusses  # noqa: E501
from swagger_server.models.trips import Trips  # noqa: E501
from swagger_server.models.vehicles import Vehicles  # noqa: E501
from swagger_server import util

from admin.import_controller import ImportController


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
    elif payload['municipality'] in ImportController.vehicle_json:
        
        municipality = payload['municipality']
        if municipality in ImportController.vehicle_json:
            return ImportController.vehicle_json[municipality]
    
    return {} 

def vehicles_status_get():  # noqa: E501
    """Query vehicle status data. Only provides vehicles with status &#x27;available&#x27;

     # noqa: E501


    :rtype: Statusses
    """
    return 'do some magic!'
