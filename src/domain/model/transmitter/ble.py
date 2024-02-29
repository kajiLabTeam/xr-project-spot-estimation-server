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

    def get_id_of_private_value(self) -> BleId:
        return self.__id

    def get_ssid_of_private_value(self) -> str:
        return self.__ssid

    def get_rssi_of_private_value(self) -> int:
        return self.__rssi
