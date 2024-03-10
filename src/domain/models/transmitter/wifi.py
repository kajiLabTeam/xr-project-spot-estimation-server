from collections import defaultdict
from typing import Dict, List

from config.const import TRANSMITTER_THRESHOLD_NUMBER
from domain.models.transmitter.wifi_id import WifiId


class Wifi:
    def __init__(
        self,
        ssid: str,
        rssi: float,
        mac_address: str,
        name: str = "",
    ):
        self.__id = WifiId()
        self.__name = name
        self.__ssid = ssid
        self.__rssi = round(rssi, 2)
        self.__mac_address = mac_address

    def get_id_of_private_value(self) -> WifiId:
        return self.__id

    def get_name_of_private_value(self) -> str:
        return self.__name

    def get_ssid_private_value(self) -> str:
        return self.__ssid

    def get_rssi_private_value(self) -> float:
        return self.__rssi

    def get_mac_address_private_value(self) -> str:
        return self.__mac_address


class WifiCollection:
    def __init__(self, wifi_list: List[Wifi] = []):
        self.__wifi_list = wifi_list

    def get_wifi_list_of_private_value(self) -> List[Wifi]:
        return self.__wifi_list

    def add_wifi(self, wifi: Wifi):
        self.__wifi_list.append(wifi)

    def remove_wifi(self, wifi: Wifi):
        self.__wifi_list.remove(wifi)

    def extract_id_wifi_collection(self) -> List[WifiId]:
        return [wifi.get_id_of_private_value() for wifi in self.__wifi_list]

    # INFO : リクエストの度に同じIDを生成するので、IDを再生成する
    def re_typing_id(self):
        self.__wifi_list = [
            Wifi(
                ssid=wifi.get_ssid_private_value(),
                rssi=wifi.get_rssi_private_value(),
                mac_address=wifi.get_mac_address_private_value(),
                name=wifi.get_name_of_private_value(),
            )
            for wifi in self.__wifi_list
        ]

    # mac_addressの一致率を計測
    def measuring_match_rates(self, wifi_collection: "WifiCollection") -> float:
        # WiFiのmac_address一致率を計測
        wifi_mac_addresses = [
            wifi.get_mac_address_private_value()
            for wifi in self.get_wifi_list_of_private_value()
        ]
        wifi_mac_match_count = sum(
            1
            for mac_address in wifi_mac_addresses
            if mac_address
            in [
                wifi.get_mac_address_private_value()
                for wifi in wifi_collection.get_wifi_list_of_private_value()
            ]
        )
        wifi_mac_match_ratio = wifi_mac_match_count / max(len(wifi_mac_addresses), 1)

        return wifi_mac_match_ratio

    # 一定数以上のデータを残し、一意なSSIDでRSSIを平均化する
    def process_wifi_collection(self) -> "WifiCollection":
        ssid_rssi_mapping: Dict[str, List[float]] = defaultdict(list)

        # SSIDを元にRSSIをグループ化
        for wifi in self.get_wifi_list_of_private_value():
            ssid_rssi_mapping[wifi.get_mac_address_private_value()].append(
                wifi.get_rssi_private_value()
            )

        processed_wifi_collection = WifiCollection()
        for ssid, rssi_list in ssid_rssi_mapping.items():
            if len(rssi_list) > TRANSMITTER_THRESHOLD_NUMBER:  # 要素数が1つのものは削除
                avg_rssi = sum(rssi_list) / len(rssi_list)  # RSSIの平均値を計算
                processed_wifi_collection.add_wifi(
                    Wifi(ssid="", rssi=avg_rssi, mac_address=ssid)
                )

        return processed_wifi_collection
