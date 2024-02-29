from domain.model.fp_model.fp_model_aggregate_id import FpModelAggregateId


class FpModelAggregate:
    def __init__(
        self,
        fp_model_file: bytes,
        extension: str,
    ):
        if len(extension) > 10:
            raise ValueError("Invalid extension")
        self.__id = FpModelAggregateId()
        self.__fp_model_file = fp_model_file
        self.__extension = extension

    def get_id_of_private_value(self) -> FpModelAggregateId:
        return self.__id

    def get_fp_model_of_private_value(self) -> bytes:
        return self.__fp_model_file

    def get_extension_of_private_value(self) -> str:
        return self.__extension

    # TODO : FPモデルの一致率を計算する処理を実装する
    def calculate_percentage_of_agreement_for_fp_model(
        self, fp_model_file: bytes
    ) -> float:
        return 100.0
