from abc import ABC, abstractmethod

from model.spot_collection.aggregate import SpotCollectionAggregate


class SpotCollectionRepository(ABC):
    @abstractmethod
    def get_spot_by_spot_id_collection(
        self, spot_id_collection: list[str]
    ) -> SpotCollectionAggregate:
        pass
