from typing import Any, List
from uuid import UUID

from domain.model.transmitter.aggregate import TransmitterAggregate
from psycopg.connection import Connection
from psycopg.rows import TupleRow
from domain.model.spot_collection.spot_collection_id import SpotCollectionId

from domain.model.fp_model.aggregate import FpModelAggregate
from domain.model.spot.spot_aggregate_id import SpotAggregateId
from domain.repository_impl.fp_model_repository_impl import \
    FpModelRepositoryImpl
from domain.repository_impl.transmitter_repository_impl import \
    TransmitterRepositoryImpl


class SpotCollectionAggregate:
    def __init__(
        self,
        spot_id_collection: List[SpotAggregateId],
    ):
        self.__id = SpotCollectionId()
        self.__spot_id_collection: List[SpotAggregateId] = spot_id_collection

    def get_id_of_private_value(self) -> SpotCollectionId:
        return self.__id

    def get_id_collection_of_private_value(self) -> List[SpotAggregateId]:
        return self.__spot_id_collection

    def add_spot_id(self, spot_id: SpotAggregateId):
        self.__spot_id_collection.append(spot_id)

    def remove_spot_id(self, spot_id: SpotAggregateId):
        self.__spot_id_collection.remove(spot_id)

    # 発信機情報を元にスポットを特定する
    def identify_spot_by_transmitter(
        self,
        conn: Connection[TupleRow],
        connecting_transmitter: TransmitterAggregate,
        transmitter_repository: TransmitterRepositoryImpl,
    ):
        # 発信機情報を元にスポットを特定する
        for spot_id in self.__spot_id_collection:
            transmitter = transmitter_repository.find_for_spot_id(
                conn=conn,
                spot_id=spot_id,
            )

            # 発信機の一致率が閾値を超えていない場合、スポットIDの集約から削除
            if not transmitter.is_match_connection(connecting_transmitter):
                self.remove_spot_id(spot_id)

    # TODO : DBに登録されているFPモデルのうち、最も近しいスポットを一意に特定する
    def identify_spot_by_fp_model(
        self,
        s3: Any,
        conn: Connection[TupleRow],
        current_fp_model: FpModelAggregate,
        fp_model_repository: FpModelRepositoryImpl,
    ) -> SpotAggregateId:
        max_agreement_rate = 0
        max_agreement_rate_spot_id: SpotAggregateId = (
            self.get_id_collection_of_private_value()[0]
        )
        # FPモデルを元にスポットを特定する
        for spot_id in self.get_id_collection_of_private_value():
            # 現在位置である可能性のあるスポットを取得
            fp_model = fp_model_repository.find_for_spot_id(
                s3=s3,
                conn=conn,
                spot_id=spot_id,
            )

            # FPモデルとの一致率が一番高いスポットを特定
            agreement_rate = fp_model.calculate_percentage_of_agreement_for_fp_model(
                current_fp_model.get_fp_model_of_private_value()
            )

            if agreement_rate > max_agreement_rate:
                max_agreement_rate = agreement_rate
                max_agreement_rate_spot_id = spot_id

        return max_agreement_rate_spot_id


class SpotCollectionAggregateFactory:
    @staticmethod
    def create(spot_id_collection: List[str]) -> SpotCollectionAggregate:
        uuid_collection: List[UUID] = []
        for spot_id in spot_id_collection:
            try:
                uuid = UUID(spot_id, version=4)
                uuid_collection.append(uuid)
            except ValueError:
                raise ValueError(f"Invalid UUID format for item_id: {spot_id}")

        return SpotCollectionAggregate(
            spot_id_collection=[SpotAggregateId(uuid) for uuid in uuid_collection]
        )
