from wifi_id import WifiId


class Wifi:
    def __init__(
        self,
        ssid: str,
        rssi: int,
    ):
        self.id = WifiId()
        self.ssid = ssid
        self.rssi = rssi
