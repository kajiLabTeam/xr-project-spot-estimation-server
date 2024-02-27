from spot_collection_id import SpotCollectionId

from domain.model.spot.spot_aggregate_id import SpotAggregateId


class SpotCollectionAggregate:
    def __init__(
        self,
        spot_id_collection: list[SpotAggregateId],
    ):
        self.__id = SpotCollectionId()
        self.__spot_id_collection = spot_id_collection

    def add_spot_id(self, spot_id: SpotAggregateId):
        self.__spot_id_collection.append(spot_id)
