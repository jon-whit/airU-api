from django.test import TestCase
from django.contrib.auth.models import User
from airu_api.models import Device

class DeviceModelTestCase(TestCase):

    def setUp(self):
        """
        Setup objects and state used across various tests.
        """
        self.user = User.objects.create(username='test-user')

    def test_device_created(self):
        """
        Test Device creation.

        This test verifies that a Device object is created and it's fields
        are set appropriately.
        """
        device = Device.objects.create(id='00:0a:95:9d:68:16', owner=self.user,
			latitude=40.4698001, longitude=-109.5696812, firmware_ver='1.0', device_revision='A') 

        self.assertEqual(device.id, '00:0a:95:9d:68:16')
        self.assertEqual(device.owner, self.user)
        self.assertEqual(device.latitude, 40.4698001)
        self.assertEqual(device.longitude, -109.5696812)
        self.assertEqual(device.firmware_ver, '1.0')
        self.assertEqual(device.device_revision, 'A')

    def test_device_delete(self):
        """
        Test Device deletion.

        Verify a single Device object is created and that the number of Device objects
        is equal to 0 after deletion.
        """
        device = Device.objects.create(id='00:0a:95:9d:68:16', owner=self.user,
                        latitude=40.4698001, longitude=-109.5696812, firmware_ver='1.0', device_revision='A')

        self.assertEqual(Device.objects.count(), 1)
        device.delete()
        self.assertEqual(Device.objects.count(), 0)
