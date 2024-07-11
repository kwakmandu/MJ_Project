from hardware_interface import FlashMemoryDevice


class DeviceDriver:
    """
    This class is used by the operating system to interact with the hardware 'FlashMemoryDevice'.
    """

    def __init__(self, device: FlashMemoryDevice):
        """
        :type device: hardware_interface.FlashMemoryDevice
        """
        self.__device = device

    def write(self, address: int, data: int) -> None:
        if self.__device.read(address) != 0:
            raise Exception('WriteFailException')

        self.__device.write(address, data)

    def read(self, address: int) -> int:
        returns = []
        for i in range(5):
            returns.append(self.__device.read(address))

        first_val = returns[0]
        if all([first_val == val for val in returns]):
            return first_val

        raise Exception("ReadFailException")
