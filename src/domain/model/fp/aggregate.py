from fp_model_id import FpModelId
from raw_data_id import RawDataId

from domain.model.fp.fp_aggregate_id import FpAggregateId


class FpAggregate:
    def __init__(
        self,
        fp_model_id: FpModelId,
        raw_data_id: RawDataId,
    ):
        self.__id = FpAggregateId()
        self.__fp_model_id = fp_model_id
        self.__raw_data_id = raw_data_id
