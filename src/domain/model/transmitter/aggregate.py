from typing import List

from ble import Ble
from ble_id import BleId
from wifi import Wifi
from wifi_id import WifiId


class TransmitterAggregate:
    def __init__(
        self,
        ble_collection: List[Ble],
        wifi_collection: List[Wifi],
    ):
        # TODO : この辺で閾値以下だったらコレクションから削除するようにする
        self.__ble_collection = ble_collection
        self.__wifi_collection = wifi_collection

    def add_ble(self, ble: Ble):
        self.__ble_collection.append(ble)

    def extract_id_ble_collection(self) -> List[BleId]:
        return [ble.get_id_of_private_value() for ble in self.__ble_collection]

    def add_wifi(self, wifi: Wifi):
        self.__wifi_collection.append(wifi)

    def extract_id_wifi_collection(self) -> List[WifiId]:
        return [wifi.get_id_of_private_value() for wifi in self.__wifi_collection]

    # TODO : BLEとWIFIのIDの一致率を計測,そして閾値を超えたらTrueを返す
    def is_match_connection(self, transmitter: "TransmitterAggregate") -> bool:
        return True
