from abc import ABC, abstractmethod

import psycopg
from model.fp.aggregate import FpAggregate
from psycopg.rows import TupleRow


class FpRepositoryImpl(ABC):
    @abstractmethod
    def get_fp_by_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: str,
    ) -> FpAggregate:
        pass

    @abstractmethod
    def create_fp(
        self,
        conn: psycopg.Connection[TupleRow],
        fp: FpAggregate,
    ):
        pass
