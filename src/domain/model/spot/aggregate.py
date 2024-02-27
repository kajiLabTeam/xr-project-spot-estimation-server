from coordinate import Coordinate
from coordinate_id import CoordinateId
from fp.fp_aggregate_id import FpAggregateId
from spot_aggregate_id import SpotAggregateId
from transmitter.transmitter_aggregate_id import TransmitterAggregateId


class SpotAggregate:
    def __init__(
        self,
        name: str,
        floors: int,
        location_type: str,
        coordinate_id: CoordinateId,
    ):
        if location_type not in ["indoor", "outdoor"]:
            raise ValueError("Invalid location type")

        self.__id = SpotAggregateId()
        self.__name = name
        self.__floors = floors
        self.__locationType = location_type
        self.__coordinate_id = coordinate_id
        self.__fp_id = ""
        self.__transmitter_id = ""

    def link_to_aggregate_fp(self, fp_id: FpAggregateId):
        self.fp_id = fp_id

    def link_to_aggregate_transmitter(self, transmitter_id: TransmitterAggregateId):
        self.transmitter_id = transmitter_id


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
        coordinate = Coordinate(latitude, longitude)
        return SpotAggregate(
            name=name,
            floors=floors,
            location_type=location_type,
            coordinate_id=coordinate.get_id_of_private_value(),
        )
