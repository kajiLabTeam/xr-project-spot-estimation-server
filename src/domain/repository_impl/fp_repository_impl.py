from abc import ABC, abstractmethod

from model.fp.aggregate import FpAggregate


class FpModelRepository(ABC):
    @abstractmethod
    def get_fp_by_spot_id(self, spot_id: str) -> FpAggregate:
        pass

    @abstractmethod
    def create_fp(self, fp: FpAggregate):
        pass
