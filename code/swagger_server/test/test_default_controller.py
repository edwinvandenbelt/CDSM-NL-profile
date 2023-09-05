# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.geofencing_zones import GeofencingZones  # noqa: E501
from swagger_server.models.iso_dayhour import IsoDayhour  # noqa: E501
from swagger_server.models.statusses import Statusses  # noqa: E501
from swagger_server.models.trips import Trips  # noqa: E501
from swagger_server.models.vehicles import Vehicles  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_geofencing_zones_get(self):
        """Test case for geofencing_zones_get

        return the operational area, according to the shared mobility provider
        """
        response = self.client.open(
            '/geofencing_zones',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_trips_end_time_get(self):
        """Test case for trips_end_time_get

        Query historical trip data.
        """
        response = self.client.open(
            '/trips/{end_time}'.format(end_time=IsoDayhour()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vehicles_get(self):
        """Test case for vehicles_get

        Query vehicle data.
        """
        response = self.client.open(
            '/vehicles',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_vehicles_status_get(self):
        """Test case for vehicles_status_get

        Query vehicle status data. Only provides vehicles with status 'available'
        """
        response = self.client.open(
            '/vehicles/status',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
