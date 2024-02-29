from coordinate import Coordinate
from fp_model.fp_model_aggregate_id import FpModelAggregateId
from location_type import LocationType
from spot_aggregate_id import SpotAggregateId
from transmitter.aggregate import TransmitterAggregate


class SpotAggregate:
    def __init__(
        self,
        id: SpotAggregateId | None,
        name: str,
        floors: int,
        location_type: LocationType,
        coordinate: Coordinate,
    ) -> None:
        if id is None:
            self.__id = SpotAggregateId()
        else:
            self.__id = id
        self.__name = name
        self.__floors = floors
        self.__locationType = location_type
        self.__coordinate = coordinate
        self.__transmitter: TransmitterAggregate | None = None
        self.__fp_id: FpModelAggregateId | None = None

    def link_to_aggregate_fp_model(self, fp_model_id: FpModelAggregateId):
        self.fp_model_id = fp_model_id

    def link_to_aggregate_transmitter(self, transmitter: TransmitterAggregate):
        self.transmitter = transmitter

    def get_id_of_private_value(self) -> SpotAggregateId:
        return self.__id

    def get_name_of_private_value(self) -> str:
        return self.__name

    def get_floors_of_private_value(self) -> int:
        return self.__floors

    def get_location_type_of_private_value(self) -> LocationType:
        return self.__locationType

    def get_coordinate_of_private_value(self) -> Coordinate:
        return self.__coordinate

    def get_fp_id_of_private_value(self) -> FpModelAggregateId:
        if self.__fp_id is None:
            raise ValueError("fp_id is not set")
        return self.__fp_id

    def get_transmitter_id_of_private_value(self) -> TransmitterAggregate:
        if self.__transmitter is None:
            raise ValueError("transmitter_id is not set")
        return self.__transmitter


# ファクトリ:特定の引数を受け取ってドメインオブジェクトを生成するメソッド
class SpotAggregateFactory:
    @staticmethod
    def create(
        name: str,
        floors: int,
        location_type: str,
        latitude: float,
        longitude: float,
    ) -> SpotAggregate:
        __coordinate = Coordinate(latitude, longitude)
        __location_type = LocationType(location_type)
        return SpotAggregate(
            id=None,
            name=name,
            floors=floors,
            location_type=__location_type,
            coordinate=__coordinate,
        )
