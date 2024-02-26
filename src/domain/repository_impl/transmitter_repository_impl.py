from abc import ABC, abstractmethod

from domain.model.transmitter.aggregate import TransmitterAggregate


class TransmitterRepository(ABC):
    @abstractmethod
    def get_transmitter_by_transmitter_id(self, spot_id: str) -> TransmitterAggregate:
        pass

    @abstractmethod
    def create_transmitter(
        self, transmitter: TransmitterAggregate
    ) -> TransmitterAggregate:
        pass
