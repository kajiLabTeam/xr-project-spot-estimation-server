from abc import ABCMeta, abstractmethod
from typing import Any

from psycopg2.extensions import connection

from domain.models.fp_model.aggregate import FpModelAggregate
from domain.models.spot.spot_id import SpotAggregateId


class FpModelRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id(
        self,
        s3: Any,
        conn: connection,
        spot_id: SpotAggregateId,
    ) -> FpModelAggregate:
        pass

    @abstractmethod
    def save(
        self,
        s3: Any,
        conn: connection,
        spot_id: SpotAggregateId,
        fp_model: FpModelAggregate,
    ) -> FpModelAggregate:
        pass
