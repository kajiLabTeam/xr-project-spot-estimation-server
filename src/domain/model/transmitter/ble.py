from ble_id import BleId


class Ble:
    def __init__(
        self,
        ssid: str,
        rssi: int,
    ):
        self.__id = BleId()
        self.__ssid = ssid
        self.__rssi = rssi
