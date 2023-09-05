# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.links import Links  # noqa: F401,E501
from swagger_server.models.vehicle import Vehicle  # noqa: F401,E501
from swagger_server import util


class Vehicles(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, version: str=None, vehicles: List[Vehicle]=None, links: Links=None):  # noqa: E501
        """Vehicles - a model defined in Swagger

        :param version: The version of this Vehicles.  # noqa: E501
        :type version: str
        :param vehicles: The vehicles of this Vehicles.  # noqa: E501
        :type vehicles: List[Vehicle]
        :param links: The links of this Vehicles.  # noqa: E501
        :type links: Links
        """
        self.swagger_types = {
            'version': str,
            'vehicles': List[Vehicle],
            'links': Links
        }

        self.attribute_map = {
            'version': 'version',
            'vehicles': 'vehicles',
            'links': 'links'
        }
        self._version = version
        self._vehicles = vehicles
        self._links = links

    @classmethod
    def from_dict(cls, dikt) -> 'Vehicles':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vehicles of this Vehicles.  # noqa: E501
        :rtype: Vehicles
        """
        return util.deserialize_model(dikt, cls)

    @property
    def version(self) -> str:
        """Gets the version of this Vehicles.


        :return: The version of this Vehicles.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this Vehicles.


        :param version: The version of this Vehicles.
        :type version: str
        """

        self._version = version

    @property
    def vehicles(self) -> List[Vehicle]:
        """Gets the vehicles of this Vehicles.


        :return: The vehicles of this Vehicles.
        :rtype: List[Vehicle]
        """
        return self._vehicles

    @vehicles.setter
    def vehicles(self, vehicles: List[Vehicle]):
        """Sets the vehicles of this Vehicles.


        :param vehicles: The vehicles of this Vehicles.
        :type vehicles: List[Vehicle]
        """

        self._vehicles = vehicles

    @property
    def links(self) -> Links:
        """Gets the links of this Vehicles.


        :return: The links of this Vehicles.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links: Links):
        """Sets the links of this Vehicles.


        :param links: The links of this Vehicles.
        :type links: Links
        """

        self._links = links
