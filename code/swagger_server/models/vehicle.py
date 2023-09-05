# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.uuid import Uuid  # noqa: F401,E501
from swagger_server.models.vehicle_type import VehicleType  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class Vehicle(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, device_id: Uuid=None, provider_id: Uuid=None, data_provider_id: Uuid=None, vehicle_id: str=None, vehicle_type: VehicleType=None, propulsion_types: List[str]=None, battery_capacity: int=None, fuel_capacity: int=None, maximum_speed: int=None):  # noqa: E501
        """Vehicle - a model defined in Swagger

        :param device_id: The device_id of this Vehicle.  # noqa: E501
        :type device_id: Uuid
        :param provider_id: The provider_id of this Vehicle.  # noqa: E501
        :type provider_id: Uuid
        :param data_provider_id: The data_provider_id of this Vehicle.  # noqa: E501
        :type data_provider_id: Uuid
        :param vehicle_id: The vehicle_id of this Vehicle.  # noqa: E501
        :type vehicle_id: str
        :param vehicle_type: The vehicle_type of this Vehicle.  # noqa: E501
        :type vehicle_type: VehicleType
        :param propulsion_types: The propulsion_types of this Vehicle.  # noqa: E501
        :type propulsion_types: List[str]
        :param battery_capacity: The battery_capacity of this Vehicle.  # noqa: E501
        :type battery_capacity: int
        :param fuel_capacity: The fuel_capacity of this Vehicle.  # noqa: E501
        :type fuel_capacity: int
        :param maximum_speed: The maximum_speed of this Vehicle.  # noqa: E501
        :type maximum_speed: int
        """
        self.swagger_types = {
            'device_id': Uuid,
            'provider_id': Uuid,
            'data_provider_id': Uuid,
            'vehicle_id': str,
            'vehicle_type': VehicleType,
            'propulsion_types': List[str],
            'battery_capacity': int,
            'fuel_capacity': int,
            'maximum_speed': int
        }

        self.attribute_map = {
            'device_id': 'device_id',
            'provider_id': 'provider_id',
            'data_provider_id': 'data_provider_id',
            'vehicle_id': 'vehicle_id',
            'vehicle_type': 'vehicle_type',
            'propulsion_types': 'propulsion_types',
            'battery_capacity': 'battery_capacity',
            'fuel_capacity': 'fuel_capacity',
            'maximum_speed': 'maximum_speed'
        }
        self._device_id = device_id
        self._provider_id = provider_id
        self._data_provider_id = data_provider_id
        self._vehicle_id = vehicle_id
        self._vehicle_type = vehicle_type
        self._propulsion_types = propulsion_types
        self._battery_capacity = battery_capacity
        self._fuel_capacity = fuel_capacity
        self._maximum_speed = maximum_speed

    @classmethod
    def from_dict(cls, dikt) -> 'Vehicle':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vehicle of this Vehicle.  # noqa: E501
        :rtype: Vehicle
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_id(self) -> Uuid:
        """Gets the device_id of this Vehicle.


        :return: The device_id of this Vehicle.
        :rtype: Uuid
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id: Uuid):
        """Sets the device_id of this Vehicle.


        :param device_id: The device_id of this Vehicle.
        :type device_id: Uuid
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def provider_id(self) -> Uuid:
        """Gets the provider_id of this Vehicle.


        :return: The provider_id of this Vehicle.
        :rtype: Uuid
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id: Uuid):
        """Sets the provider_id of this Vehicle.


        :param provider_id: The provider_id of this Vehicle.
        :type provider_id: Uuid
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def data_provider_id(self) -> Uuid:
        """Gets the data_provider_id of this Vehicle.


        :return: The data_provider_id of this Vehicle.
        :rtype: Uuid
        """
        return self._data_provider_id

    @data_provider_id.setter
    def data_provider_id(self, data_provider_id: Uuid):
        """Sets the data_provider_id of this Vehicle.


        :param data_provider_id: The data_provider_id of this Vehicle.
        :type data_provider_id: Uuid
        """

        self._data_provider_id = data_provider_id

    @property
    def vehicle_id(self) -> str:
        """Gets the vehicle_id of this Vehicle.

        A unique vehicle identifier (visible code, license plate, etc), visible on the vehicle itself  # noqa: E501

        :return: The vehicle_id of this Vehicle.
        :rtype: str
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id: str):
        """Sets the vehicle_id of this Vehicle.

        A unique vehicle identifier (visible code, license plate, etc), visible on the vehicle itself  # noqa: E501

        :param vehicle_id: The vehicle_id of this Vehicle.
        :type vehicle_id: str
        """
        if vehicle_id is None:
            raise ValueError("Invalid value for `vehicle_id`, must not be `None`")  # noqa: E501

        self._vehicle_id = vehicle_id

    @property
    def vehicle_type(self) -> VehicleType:
        """Gets the vehicle_type of this Vehicle.


        :return: The vehicle_type of this Vehicle.
        :rtype: VehicleType
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type: VehicleType):
        """Sets the vehicle_type of this Vehicle.


        :param vehicle_type: The vehicle_type of this Vehicle.
        :type vehicle_type: VehicleType
        """
        if vehicle_type is None:
            raise ValueError("Invalid value for `vehicle_type`, must not be `None`")  # noqa: E501

        self._vehicle_type = vehicle_type

    @property
    def propulsion_types(self) -> List[str]:
        """Gets the propulsion_types of this Vehicle.


        :return: The propulsion_types of this Vehicle.
        :rtype: List[str]
        """
        return self._propulsion_types

    @propulsion_types.setter
    def propulsion_types(self, propulsion_types: List[str]):
        """Sets the propulsion_types of this Vehicle.


        :param propulsion_types: The propulsion_types of this Vehicle.
        :type propulsion_types: List[str]
        """
        allowed_values = ["human", "electric_assist", "electric", "combustion", "combustion_diesel", "hybrid", "hydrogen_fuel_cell", "plug_in_hybrid"]  # noqa: E501
        if not set(propulsion_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `propulsion_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(propulsion_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._propulsion_types = propulsion_types

    @property
    def battery_capacity(self) -> int:
        """Gets the battery_capacity of this Vehicle.

        Required if Available Capacity of battery expressed as milliamp hours (mAh)  # noqa: E501

        :return: The battery_capacity of this Vehicle.
        :rtype: int
        """
        return self._battery_capacity

    @battery_capacity.setter
    def battery_capacity(self, battery_capacity: int):
        """Sets the battery_capacity of this Vehicle.

        Required if Available Capacity of battery expressed as milliamp hours (mAh)  # noqa: E501

        :param battery_capacity: The battery_capacity of this Vehicle.
        :type battery_capacity: int
        """

        self._battery_capacity = battery_capacity

    @property
    def fuel_capacity(self) -> int:
        """Gets the fuel_capacity of this Vehicle.

        Required if Available Capacity of fuel tank (liquid, solid, gaseous) expressed in liters  # noqa: E501

        :return: The fuel_capacity of this Vehicle.
        :rtype: int
        """
        return self._fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, fuel_capacity: int):
        """Sets the fuel_capacity of this Vehicle.

        Required if Available Capacity of fuel tank (liquid, solid, gaseous) expressed in liters  # noqa: E501

        :param fuel_capacity: The fuel_capacity of this Vehicle.
        :type fuel_capacity: int
        """

        self._fuel_capacity = fuel_capacity

    @property
    def maximum_speed(self) -> int:
        """Gets the maximum_speed of this Vehicle.

        Required if Available Maximum speed (kph) possible with vehicle under normal, flat incline, smooth surface conditions. Applicable if the device has a built-in or intelligent speed limiter/governor.  # noqa: E501

        :return: The maximum_speed of this Vehicle.
        :rtype: int
        """
        return self._maximum_speed

    @maximum_speed.setter
    def maximum_speed(self, maximum_speed: int):
        """Sets the maximum_speed of this Vehicle.

        Required if Available Maximum speed (kph) possible with vehicle under normal, flat incline, smooth surface conditions. Applicable if the device has a built-in or intelligent speed limiter/governor.  # noqa: E501

        :param maximum_speed: The maximum_speed of this Vehicle.
        :type maximum_speed: int
        """

        self._maximum_speed = maximum_speed
