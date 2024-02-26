from spot.spot_id import SpotId
from spot_collection_id import SpotCollectionId


class SpotCollectionAggregate:
    def __init__(
        self,
        spot_id_collection: list[SpotId],
    ):
        self.id = SpotCollectionId()
        self.spot_id_collection = spot_id_collection

    def add_spot_id(self, spot_id: SpotId):
        self.spot_id_collection.append(spot_id)
