from abc import ABCMeta, abstractmethod
from typing import List

import psycopg
from model.spot_collection.aggregate import SpotCollectionAggregate
from psycopg.rows import TupleRow


class SpotCollectionRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id_collection(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id_collection: List[str],
    ) -> SpotCollectionAggregate:
        pass
