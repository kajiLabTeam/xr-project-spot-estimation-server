from abc import ABCMeta, abstractmethod
from typing import List

import psycopg
from psycopg.rows import TupleRow

from domain.model.spot.spot_aggregate_id import SpotAggregateId
from domain.model.transmitter.aggregate import TransmitterAggregate
from domain.model.transmitter.ble import Ble
from domain.model.transmitter.wifi import Wifi


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
