from typing import Any

import psycopg
from psycopg.rows import TupleRow

from domain.model.fp_model.aggregate import FpModelAggregate
from domain.model.spot.spot_aggregate_id import SpotAggregateId
from domain.repository_impl.fp_model_repository_impl import \
    FpModelRepositoryImpl


# TODO : このクラスを実装する
class FpModelRepository(FpModelRepositoryImpl):
    def find_for_spot_id(
        self,
        s3: Any,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
    ) -> FpModelAggregate:
        return FpModelAggregate(
            b"fp_model_file",
            "extension",
        )

    def save(
        self,
        s3: Any,
        conn: psycopg.Connection[TupleRow],
        spot_id: SpotAggregateId,
        fp_model: FpModelAggregate,
    ) -> FpModelAggregate:
        return FpModelAggregate(
            b"fp_model_file",
            "extension",
        )
