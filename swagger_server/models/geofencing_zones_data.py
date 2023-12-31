# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.feature_collection import FeatureCollection  # noqa: F401,E501
from swagger_server import util


class GeofencingZonesData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, geofencing_zones: FeatureCollection=None):  # noqa: E501
        """GeofencingZonesData - a model defined in Swagger

        :param geofencing_zones: The geofencing_zones of this GeofencingZonesData.  # noqa: E501
        :type geofencing_zones: FeatureCollection
        """
        self.swagger_types = {
            'geofencing_zones': FeatureCollection
        }

        self.attribute_map = {
            'geofencing_zones': 'geofencing_zones'
        }
        self._geofencing_zones = geofencing_zones

    @classmethod
    def from_dict(cls, dikt) -> 'GeofencingZonesData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The geofencing_zones_data of this GeofencingZonesData.  # noqa: E501
        :rtype: GeofencingZonesData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def geofencing_zones(self) -> FeatureCollection:
        """Gets the geofencing_zones of this GeofencingZonesData.


        :return: The geofencing_zones of this GeofencingZonesData.
        :rtype: FeatureCollection
        """
        return self._geofencing_zones

    @geofencing_zones.setter
    def geofencing_zones(self, geofencing_zones: FeatureCollection):
        """Sets the geofencing_zones of this GeofencingZonesData.


        :param geofencing_zones: The geofencing_zones of this GeofencingZonesData.
        :type geofencing_zones: FeatureCollection
        """

        self._geofencing_zones = geofencing_zones
