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
