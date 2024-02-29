from typing import List

from domain.model.fp_model.aggregate import FpModelAggregate
from domain.model.raw_data.raw_data_aggregate_id import RawDataId
from domain.model.transmitter.ble import Ble
from domain.model.transmitter.wifi import Wifi


class RawDataAggregate:
    def __init__(
        self,
        raw_data_file: bytes,
    ):
        self.__id = RawDataId()
        self.__raw_data_file = raw_data_file

    def get_id_private_value(self) -> RawDataId:
        return self.__id

    def get_raw_data_private_value(self) -> bytes:
        return self.__raw_data_file

    # TODO : CSVファイルからFPモデルを生成する処理を実装する
    def generate_fp_model(self) -> FpModelAggregate:
        return FpModelAggregate(
            fp_model_file=self.__raw_data_file,
            extension="csv",
        )

    # TODO : CSVファイルから接続中のBLEを抽出する処理を実装する
    def extract_ble_collection(self) -> List[Ble]:
        return list(
            [
                Ble(
                    ssid="ble_id",
                    rssi=-50,
                )
            ]
        )

    # TODO : CSVファイルから接続中のWIFIを抽出する処理を実装する
    def extract_wifi_collection(self) -> List[Wifi]:
        return list(
            [
                Wifi(
                    ssid="wifi_id",
                    rssi=-50,
                )
            ]
        )


class RawDataAggregateFactory:
    @staticmethod
    def create(
        raw_data_file: bytes,
    ) -> RawDataAggregate:
        return RawDataAggregate(
            raw_data_file=raw_data_file,
        )
