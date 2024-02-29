from fp_model_aggregate_id import FpModelAggregateId
from psycopg import Connection
from psycopg.rows import TupleRow
from spot_collection.aggregate import SpotCollectionAggregate

from domain.repository_impl.spot_repository_impl import SpotRepositoryImpl


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

    # TODO : FPモデルとの一致度が最も高いFPモデル集約を取得する処理を実装する
    def get_highest_rate_of_agreement_with_fp_model(
        self,
        conn: Connection[TupleRow],
        spot_repository: SpotRepositoryImpl,
        fp_model: "FpModelAggregate",
        spot_id_collection: SpotCollectionAggregate,
    ) -> "FpModelAggregate":
        max_agreement_rate = 0
        result_fp_model = None
        # FPモデルを元にスポットを特定する
        for spot_id in spot_id_collection.get_id_collection_of_private_value():
            spot = spot_repository.find_for_spot_id(conn=conn, spot_id=spot_id)
            agreement_rate = self.calculate_percentage_of_agreement_for_fp_model(
                fp_model.get_fp_model_of_private_value()
            )
            # FPモデルとの一致率が一番高いスポットを特定
            if agreement_rate > max_agreement_rate:
                max_agreement_rate = agreement_rate
