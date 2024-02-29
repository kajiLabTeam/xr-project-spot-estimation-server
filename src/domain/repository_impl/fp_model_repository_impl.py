from abc import ABCMeta, abstractmethod
from typing import Any

import psycopg
from model.fp_model.aggregate import FpModelAggregate
from model.spot.spot_aggregate_id import SpotAggregateId
from psycopg.rows import TupleRow


class FpModelRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id(
        self,
        s3: Any,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> FpModelAggregate:
        pass

    @abstractmethod
    def save(
        self,
        s3: Any,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
        fp_model: FpModelAggregate,
    ) -> FpModelAggregate:
        pass
