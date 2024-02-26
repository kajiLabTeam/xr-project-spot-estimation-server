from ble_id import BleId
from transmitter_id import TransmitterId
from wifi_id import WifiId


class TransmitterAggregate:
    def __init__(
        self,
        wifi_id_collection: list[WifiId],
        ble_id_collection: list[BleId],
    ):
        self.id = TransmitterId()
        self.wifi_id_collection = wifi_id_collection
        self.ble_id_collection = ble_id_collection

    def add_wifi_id(self, wifi_id: WifiId):
        self.wifi_id_collection.append(wifi_id)

    def add_ble_id(self, ble_id: BleId):
        self.ble_id_collection.append(ble_id)
