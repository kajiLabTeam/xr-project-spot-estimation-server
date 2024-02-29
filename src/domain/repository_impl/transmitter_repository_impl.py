from abc import ABCMeta, abstractmethod
from typing import List

import psycopg
from model.spot.spot_aggregate_id import SpotAggregateId
from model.transmitter.aggregate import TransmitterAggregate
from model.transmitter.ble import Ble
from model.transmitter.wifi import Wifi
from psycopg.rows import TupleRow


class TransmitterRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> TransmitterAggregate:
        pass

    @abstractmethod
    def save(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
        ble_collection: List[Ble],
        wifi_collection: List[Wifi],
    ) -> TransmitterAggregate:
        pass
