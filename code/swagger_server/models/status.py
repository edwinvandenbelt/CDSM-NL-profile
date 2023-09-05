# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.event import Event  # noqa: F401,E501
from swagger_server.models.telemetry import Telemetry  # noqa: F401,E501
from swagger_server.models.uuid import Uuid  # noqa: F401,E501
import re  # noqa: F401,E501
from swagger_server import util


class Status(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, device_id: Uuid=None, provider_id: Uuid=None, last_event: Event=None, last_telemetry: Telemetry=None):  # noqa: E501
        """Status - a model defined in Swagger

        :param device_id: The device_id of this Status.  # noqa: E501
        :type device_id: Uuid
        :param provider_id: The provider_id of this Status.  # noqa: E501
        :type provider_id: Uuid
        :param last_event: The last_event of this Status.  # noqa: E501
        :type last_event: Event
        :param last_telemetry: The last_telemetry of this Status.  # noqa: E501
        :type last_telemetry: Telemetry
        """
        self.swagger_types = {
            'device_id': Uuid,
            'provider_id': Uuid,
            'last_event': Event,
            'last_telemetry': Telemetry
        }

        self.attribute_map = {
            'device_id': 'device_id',
            'provider_id': 'provider_id',
            'last_event': 'last_event',
            'last_telemetry': 'last_telemetry'
        }
        self._device_id = device_id
        self._provider_id = provider_id
        self._last_event = last_event
        self._last_telemetry = last_telemetry

    @classmethod
    def from_dict(cls, dikt) -> 'Status':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The status of this Status.  # noqa: E501
        :rtype: Status
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_id(self) -> Uuid:
        """Gets the device_id of this Status.


        :return: The device_id of this Status.
        :rtype: Uuid
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id: Uuid):
        """Sets the device_id of this Status.


        :param device_id: The device_id of this Status.
        :type device_id: Uuid
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def provider_id(self) -> Uuid:
        """Gets the provider_id of this Status.


        :return: The provider_id of this Status.
        :rtype: Uuid
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id: Uuid):
        """Sets the provider_id of this Status.


        :param provider_id: The provider_id of this Status.
        :type provider_id: Uuid
        """
        if provider_id is None:
            raise ValueError("Invalid value for `provider_id`, must not be `None`")  # noqa: E501

        self._provider_id = provider_id

    @property
    def last_event(self) -> Event:
        """Gets the last_event of this Status.


        :return: The last_event of this Status.
        :rtype: Event
        """
        return self._last_event

    @last_event.setter
    def last_event(self, last_event: Event):
        """Sets the last_event of this Status.


        :param last_event: The last_event of this Status.
        :type last_event: Event
        """
        if last_event is None:
            raise ValueError("Invalid value for `last_event`, must not be `None`")  # noqa: E501

        self._last_event = last_event

    @property
    def last_telemetry(self) -> Telemetry:
        """Gets the last_telemetry of this Status.


        :return: The last_telemetry of this Status.
        :rtype: Telemetry
        """
        return self._last_telemetry

    @last_telemetry.setter
    def last_telemetry(self, last_telemetry: Telemetry):
        """Sets the last_telemetry of this Status.


        :param last_telemetry: The last_telemetry of this Status.
        :type last_telemetry: Telemetry
        """
        if last_telemetry is None:
            raise ValueError("Invalid value for `last_telemetry`, must not be `None`")  # noqa: E501

        self._last_telemetry = last_telemetry
