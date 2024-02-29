from abc import ABCMeta, abstractmethod
from typing import Any

import psycopg
from model.raw_data.aggregate import RawDataAggregate
from model.spot.spot_aggregate_id import SpotAggregateId
from psycopg.rows import TupleRow


class RawDataRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> RawDataAggregate:
        pass

    @abstractmethod
    def save(
        self,
        s3: Any,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
        raw_data: RawDataAggregate,
    ) -> RawDataAggregate:
        pass
