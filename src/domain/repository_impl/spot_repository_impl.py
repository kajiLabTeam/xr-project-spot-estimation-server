from abc import ABC, abstractmethod

import psycopg
from model.spot.aggregate import SpotAggregate
from psycopg.rows import TupleRow


class SpotRepositoryImpl(ABC):
    @abstractmethod
    def create_spot(
        self,
        conn: psycopg.Connection[TupleRow],
        spot: SpotAggregate,
    ) -> SpotAggregate:
        pass

    @abstractmethod
    def get_spot_by_spot_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: str,
    ) -> SpotAggregate:
        pass
