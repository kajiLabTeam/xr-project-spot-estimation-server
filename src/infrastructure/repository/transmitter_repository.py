from typing import List

import psycopg
from psycopg.rows import TupleRow

from domain.model.spot.spot_aggregate_id import SpotAggregateId
from domain.model.transmitter.aggregate import TransmitterAggregate
from domain.model.transmitter.ble import Ble
from domain.model.transmitter.wifi import Wifi
from domain.repository_impl.transmitter_repository_impl import \
    TransmitterRepositoryImpl


# TODO : このクラスを実装する
class TransmitterRepository(TransmitterRepositoryImpl):
    def find_for_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> TransmitterAggregate:
        return TransmitterAggregate(
            [
                Ble(
                    "ble_ssid",
                    -90,
                ),
            ],
            [
                Wifi(
                    "wifi_ssid",
                    -90,
                ),
            ],
        )

    def save(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
        ble_collection: List[Ble],
        wifi_collection: List[Wifi],
    ) -> TransmitterAggregate:
        return TransmitterAggregate(
            [
                Ble(
                    "ble_ssid",
                    -90,
                ),
            ],
            [
                Wifi(
                    "wifi_ssid",
                    -90,
                ),
            ],
        )
