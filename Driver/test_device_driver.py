from unittest import TestCase
from unittest.mock import Mock
from hardware_interface import FlashMemoryDevice
from device_driver import DeviceDriver

ADDRESS = 0xFF
NO_WRITE_DATA = 0
SUCCESSFUL_READ_DATA = [10] * 5
UNSUCCESSFUL_READ_DATA = [10] * 2 + [15] + [10] * 2
WRITE_DATA = 15


class DeviceDriverTest(TestCase):
    def setUp(self):
        self.hardware: FlashMemoryDevice = Mock()
        self.driver = DeviceDriver(self.hardware)

    def test_successful_read(self):
        self.hardware.read.side_effect = SUCCESSFUL_READ_DATA
        self.assertEqual(SUCCESSFUL_READ_DATA[0], self.driver.read(ADDRESS))

    def test_unsuccessful_read(self):
        self.hardware.read.side_effect = UNSUCCESSFUL_READ_DATA

        with self.assertRaises(Exception) as e:
            self.driver.read(ADDRESS)
            self.fail()
        self.assertEqual("ReadFailException", str(e.exception))

    def test_successful_write(self):
        self.hardware.read.side_effect = [NO_WRITE_DATA] + [WRITE_DATA] * 5
        self.driver.write(ADDRESS, WRITE_DATA)
        self.assertEqual(WRITE_DATA, self.driver.read(ADDRESS))

    def test_unsuccessful_write(self):
        self.hardware.read.side_effect = [WRITE_DATA] + [WRITE_DATA] * 5
        with self.assertRaises(Exception) as e:
            self.driver.write(ADDRESS, WRITE_DATA)
            self.fail()
        self.assertEqual("WriteFailException", str(e.exception))
