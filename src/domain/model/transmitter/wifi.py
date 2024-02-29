from wifi_id import WifiId


class Wifi:
    def __init__(
        self,
        ssid: str,
        rssi: int,
    ):
        self.__id = WifiId()
        self.__ssid = ssid
        self.__rssi = rssi

    def get_id_of_private_value(self) -> WifiId:
        return self.__id

    def get_ssid_private_value(self) -> str:
        return self.__ssid

    def get_rssi_private_value(self) -> int:
        return self.__rssi
