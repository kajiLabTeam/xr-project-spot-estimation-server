from domain.model.raw_data.aggregate import RawDataAggregate
from domain.model.spot.aggregate import SpotAggregate
from domain.model.spot_collection.aggregate import SpotCollectionAggregate
from domain.model.transmitter.aggregate import TransmitterAggregate
from domain.repository_impl.fp_model_repository_impl import FpModelRepositoryImpl
from domain.repository_impl.spot_repository_impl import SpotRepositoryImpl
from domain.repository_impl.transmitter_repository_impl import TransmitterRepositoryImpl
from infrastructure.connection import DBConnection, MinioConnection

conn = DBConnection().connect()
s3 = MinioConnection().connect()


class GetSpotBySpotIdCollectionService:
    def __init__(
        self,
        spot_repository: SpotRepositoryImpl,
        fp_model_repository: FpModelRepositoryImpl,
        transmitter_repository: TransmitterRepositoryImpl,
    ):
        self.__spot_repository = spot_repository
        self.__fp_model_repository = fp_model_repository
        self.__transmitter_repository = transmitter_repository

    def run(
        self,
        raw_data: RawDataAggregate,
        spot_collection: SpotCollectionAggregate,
    ) -> SpotAggregate | None:
        # 生データからFPモデルを生成
        fp_model = raw_data.generate_fp_model()
        # 接続中のBLEを抽出
        connecting_ble_collection = raw_data.extract_ble_collection()
        # 接続中のWIFIを抽出
        connecting_wifi_collection = raw_data.extract_wifi_collection()

        # 接続中のBLE、WIFIを元に発信機集約のインスタンスを作成
        connecting_transmitter = TransmitterAggregate(
            ble_collection=connecting_ble_collection,
            wifi_collection=connecting_wifi_collection,
        )

        # 発信機情報を元にスポットを特定する
        spot_collection.identify_spot_by_transmitter(
            conn=conn,
            connecting_transmitter=connecting_transmitter,
            transmitter_repository=self.__transmitter_repository,
        )

        # 現在位置にスポットが存在しない場合
        if len(spot_collection.get_id_collection_of_private_value()) == 0:
            return None

        # 発信機情報のみで単一のスポットが特定できた場合
        if len(spot_collection.get_id_collection_of_private_value()) == 1:
            spot = self.__spot_repository.find_for_spot_id(
                conn=conn,
                spot_id=spot_collection.get_id_collection_of_private_value()[0],
            )
            return spot

        # FPモデルを元にスポットを特定する
        spot_id = spot_collection.identify_spot_by_fp_model(
            s3=s3,
            conn=conn,
            current_fp_model=fp_model,
            fp_model_repository=self.__fp_model_repository,
        )

        spot = self.__spot_repository.find_for_spot_id(
            conn=conn,
            spot_id=spot_id,
        )

        return spot
