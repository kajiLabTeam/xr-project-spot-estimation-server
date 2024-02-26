from ble_id import BleId


class Ble:
    def __init__(
        self,
        ssid: str,
        rssi: int,
    ):
        self.id = BleId()
        self.ssid = ssid
        self.rssi = rssi
