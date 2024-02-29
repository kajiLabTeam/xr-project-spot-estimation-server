from abc import ABCMeta, abstractmethod

import psycopg
from psycopg.rows import TupleRow

from domain.model.fp_model.fp_model_aggregate_id import FpModelAggregateId
from domain.model.spot.aggregate import SpotAggregate
from domain.model.spot.spot_aggregate_id import SpotAggregateId


class SpotRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> SpotAggregate:
        pass

    @abstractmethod
    def find_for_fp_model_id(
        self,
        conn: psycopg.Connection[TupleRow],
        fp_model_id: FpModelAggregateId,
    ) -> SpotAggregate:
        pass

    @abstractmethod
    def save(
        self,
        conn: psycopg.Connection[TupleRow],
        spot: SpotAggregate,
    ) -> SpotAggregate:
        pass
