from typing import Any

import psycopg
from psycopg.rows import TupleRow

from domain.model.raw_data.aggregate import RawDataAggregate
from domain.model.spot.spot_aggregate_id import SpotAggregateId
from domain.repository_impl.raw_data_repository_impl import \
    RawDataRepositoryImpl


# TODO : このクラスを実装する
class RawDataRepository(RawDataRepositoryImpl):
    def find_for_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> RawDataAggregate:
        return RawDataAggregate(
            b"raw_data_file",
        )

    def save(
        self,
        s3: Any,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
        raw_data: RawDataAggregate,
    ) -> RawDataAggregate:
        return RawDataAggregate(
            b"raw_data_file",
        )
