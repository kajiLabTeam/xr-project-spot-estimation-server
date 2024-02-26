from abc import ABC, abstractmethod

from model.spot.aggregate import SpotAggregate


class SpotRepository(ABC):
    @abstractmethod
    def create_spot(self, spot: SpotAggregate) -> SpotAggregate:
        pass

    @abstractmethod
    def get_spot_by_spot_id(self, spot_id: str) -> SpotAggregate:
        pass
