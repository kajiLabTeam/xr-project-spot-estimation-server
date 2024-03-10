from abc import ABCMeta, abstractmethod
from typing import Any

from psycopg2.extensions import connection

from domain.models.raw_data.aggregate import RawDataAggregate
from domain.models.spot.spot_id import SpotAggregateId


class RawDataRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id(
        self,
        s3: Any,
        conn: connection,
        spot_id: SpotAggregateId,
    ) -> RawDataAggregate:
        pass

    @abstractmethod
    def save(
        self,
        s3: Any,
        conn: connection,
        spot_id: SpotAggregateId,
        raw_data: RawDataAggregate,
    ) -> RawDataAggregate:
        pass
