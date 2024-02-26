from fp_id import FpId
from fp_model_id import FpModelId
from raw_data_id import RawDataId


class FpAggregate:
    def __init__(
        self,
        fp_model_id: FpModelId,
        raw_data_id: RawDataId,
    ):
        self.id = FpId()
        self.fp_model_id = fp_model_id
        self.raw_data_id = raw_data_id
