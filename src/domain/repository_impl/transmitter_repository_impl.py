from abc import ABCMeta, abstractmethod

from psycopg2.extensions import connection

from domain.models.spot.spot_id import SpotAggregateId
from domain.models.transmitter.aggregate import TransmitterAggregate


class TransmitterRepositoryImpl(metaclass=ABCMeta):
    @abstractmethod
    def find_for_spot_id(
        self,
        conn: connection,
        spot_id: SpotAggregateId,
    ) -> TransmitterAggregate:
        pass

    @abstractmethod
    def save(
        self,
        conn: connection,
        spot_id: SpotAggregateId,
        transmitter: TransmitterAggregate,
    ) -> TransmitterAggregate:
        pass
