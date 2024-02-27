from ble_id import BleId
from wifi_id import WifiId

from domain.model.transmitter.transmitter_aggregate_id import \
    TransmitterAggregateId


class TransmitterAggregate:
    def __init__(
        self,
        wifi_id_collection: list[WifiId],
        ble_id_collection: list[BleId],
    ):
        self.__id = TransmitterAggregateId()
        self.__wifi_id_collection = wifi_id_collection
        self.__ble_id_collection = ble_id_collection

    def add_wifi_id(self, wifi_id: WifiId):
        self.__wifi_id_collection.append(wifi_id)

    def add_ble_id(self, ble_id: BleId):
        self.__ble_id_collection.append(ble_id)
