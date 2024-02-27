from abc import ABC, abstractmethod

import psycopg
from model.spot_collection.aggregate import SpotCollectionAggregate
from psycopg.rows import TupleRow


class SpotCollectionRepositoryImpl(ABC):
    @abstractmethod
    def get_spot_by_spot_id_collection(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id_collection: list[str],
    ) -> SpotCollectionAggregate:
        pass
