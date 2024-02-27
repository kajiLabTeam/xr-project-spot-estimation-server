from abc import ABC, abstractmethod

import psycopg
from psycopg.rows import TupleRow

from domain.model.transmitter.aggregate import TransmitterAggregate


class TransmitterRepositoryImpl(ABC):
    @abstractmethod
    def get_transmitter_by_transmitter_id(
        self,
        conn: psycopg.Connection[TupleRow],
        spot_id: str,
    ) -> TransmitterAggregate:
        pass

    @abstractmethod
    def create_transmitter(
        self,
        conn: psycopg.Connection[TupleRow],
        transmitter: TransmitterAggregate,
    ) -> TransmitterAggregate:
        pass
